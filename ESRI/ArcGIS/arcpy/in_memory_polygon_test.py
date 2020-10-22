import arcpy

in_mem_polygon_fc = r'in_memory\polygon_to_cut'

if arcpy.Exists(in_mem_polygon_fc):
    print('before: this workspace exists: {}'.format(in_mem_polygon_fc))
    arcpy.Delete_management(in_mem_polygon_fc)
else:
    print('before: DNE')


spatial_ref = arcpy.SpatialReference(4326) # WGS 1984

# create a new feature class in memory
arcpy.CreateFeatureclass_management(out_path='in_memory', out_name='polygon_to_cut', geometry_type='POLYGON', template=None, has_m='DISABLED', has_z='DISABLED', spatial_reference=spatial_ref)

# create a test polygon
polygon_coords = [
    [-121.61775581499995, 36.75887873200003],
    [-121.61692451099998, 36.75840343100003],
    [-121.61738840799995, 36.75783622600005],
    [-121.61820810999996, 36.75828153800006],
    [-121.61775581499995, 36.75887873200003]
]

array = []
for coord in polygon_coords:
    point = arcpy.Point(coord[0], coord[1])
    array.append(point)

rings = arcpy.Array(array)

polygon = arcpy.Polygon(rings, spatial_ref)

# try inserting the polygon into the in_memory fc
with arcpy.da.InsertCursor(in_mem_polygon_fc, ['SHAPE@']) as cursor:
    insert = [polygon]
    cursor.insertRow(insert)

# try printing out the polygon as a sanity check
with arcpy.da.SearchCursor(in_mem_polygon_fc, ['SHAPE@']) as cursor:
    for row in cursor:
        print('sanity check:')
        print(row[0].JSON)

if arcpy.Exists(in_mem_polygon_fc):
    print('after: this workspace exists: {}'.format(in_mem_polygon_fc))
    arcpy.Delete_management(in_mem_polygon_fc)
else:
    print('after: DNE')

arcpy.Delete_management("in_memory")

if arcpy.Exists(in_mem_polygon_fc):
    print('after deleting: this workspace exists: {}'.format(in_mem_polygon_fc))
    arcpy.Delete_management(in_mem_polygon_fc)
else:
    print('after deleting: DNE')