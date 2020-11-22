'''

Create a child feature in one feature class and link it to its parent in another feature class. They are linked by a relationship class.

'''

import arcpy, json

fc = r"D:\SCRAPWORK\TEST.sde\egdb.TEST.BLOCKS"
where = "OBJECTID IN (15683)"

arcpy.MakeFeatureLayer_management(fc, 'test_layer', where_clause=where)

block_global_id = None
block_shape = None

with arcpy.da.SearchCursor('test_layer',  ["OID@", "SHAPE@", "GlobalID", "BLOCK_NUMBER"]) as cursor:

    for row in cursor:
        # print(row)
        print('OBJECTID: {}'.format(row[0]))
        print('SHAPE: {}'.format(row[1]))
        print('GlobalID: {}'.format(row[2]))

        block_global_id = row[2]
        block_shape = row[1]

print('')




tunnels_fc = r"D:\SCRAPWORK\TEST.sde\egdb.TEST.TUNNELS"

field_data = arcpy.ListFields(tunnels_fc)

field_index_lookup = {}

for i in range(len(field_data)):
    field = field_data[i].name
    field_index_lookup[field] = i

for key in sorted(field_index_lookup):
    print('{} : {}'.format(key, field_index_lookup[key]))


fields = [
    'SHAPE@',
    'PARENT_ID'
]


print('block_shape: {}'.format(block_shape))
print('block_global_id: {}'.format(block_global_id))


with arcpy.da.InsertCursor(tunnels_fc, fields) as cursor:
    insert = [block_shape, block_global_id]
    cursor.insertRow(insert)

