import arcpy, sys, os, datetime

# set up for environment
environment = os.environ["APP_ENVIRONMENT"]
gdb_number = os.environ["GDB_NUMBER"]

if environment == "DEV":
    connection = r"C:\DatabaseConnection\DEV_{0}.sde\DB.AWS.".format(gdb_number)
elif environment == "TEST":
    connection = r"C:\DatabaseConnection\TEST_{0}.sde\DB.AWS.".format(gdb_number)

ranches_fc = connection + 'RANCHES'
blocks_fc = connection + 'APPLICATION_BLOCKS'

ranch_id = 2510

where = 'OBJECTID = {}'.format(ranch_id)

ranch_global_id = None

with arcpy.da.SearchCursor(ranches_fc, ['GlobalID'], where_clause=where) as sc:
    for row in sc:
        ranch_global_id = row[0]

if not ranch_global_id:
    print('No GlobalID found for RANCH_ID: {}, TRANSACTIONAL_RANCH_NUMBER: {}'.format(ranch_id, transactional_ranch_number))
    sys.exit()


block_data = {
    "rings":[
        [
            [-121.59096076299994,36.689725615000043],
            [-121.59128334099995,36.690103296000075],
            [-121.59057437399997,36.690506652000067],
            [-121.59018839299995,36.690125346000059],
            [-121.59096076299994,36.689725615000043]
        ]
    ],
    "spatialReference":
        {
            "wkid" : 4326,
            "latestWkid" : 4326
        }
}

spatial_ref = arcpy.SpatialReference(block_data['spatialReference']['wkid'])

# note: we are assuming that there is just one ring
array = []
for coord in block_data['rings'][0]:
    point = arcpy.Point(coord[0], coord[1])
    array.append(point)

rings = arcpy.Array(array)

polygon = arcpy.Polygon(rings, spatial_ref)


with arcpy.da.InsertCursor(blocks_fc, ['SHAPE@', 'BLOCK_NAME', 'PARENT_ID', 'IS_ACTIVE']) as cursor:

    for i in range(0,10):
        block_name = 'PYTHON TEST {}'.format(i)
        is_active = 1 # 1 = yes 2 = no

        insert = [polygon, block_name, ranch_global_id, is_active]

        start_time = datetime.datetime.now()
        cursor.insertRow(insert)
        end_time = datetime.datetime.now()

        print('time elapsed to insert: {}'.format(end_time - start_time))
