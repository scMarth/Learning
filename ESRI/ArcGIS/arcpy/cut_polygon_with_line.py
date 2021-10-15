'''

takes the polygon in testPolygons.shp and cuts it using the cutting line in testCuttingLine.shp

because the waylines and application blocks have different spatial references, polyline is projected into proojectedLines.shp, this is the line that is used in the actual cut operation

'''



import arcpy, json, os, shutil

fc = r"C:\Users\test-user\SCRAPWORK\testPolygons\testPolygons.shp"
where = 'FID IN (0)'

arcpy.MakeFeatureLayer_management(fc, 'polygon_layer', where_clause=where)
polygon = None
with arcpy.da.SearchCursor('polygon_layer',  ["OID@", "SHAPE@"]) as cursor:
    for row in cursor:
        polygon = row[1]

fc = r"C:\Users\test-user\SCRAPWORK\testCuttingLine\testCuttingLine.shp"
where = 'FID in (0)'
arcpy.MakeFeatureLayer_management(fc, 'polyline_layer', where_clause=where)
polyline = None
with arcpy.da.SearchCursor('polyline_layer',  ["OID@", "SHAPE@"]) as cursor:
    for row in cursor:
        polyline = row[1]

print(polygon.JSON)
print(polyline.JSON)



sr = polygon.spatialReference
print("sr:")
print(sr)
print('')
basepath = os.path.dirname(os.path.abspath(__file__))
shp_path = basepath + r'\projectedLines\projectedLines.shp'
shp_folder = basepath + r'\projectedLines'

if os.path.exists(shp_folder):
    shutil.rmtree(shp_folder) 
os.mkdir(shp_folder)

# arcpy.MakeFeatureLayer_management('polyline_layer', 'projected_polylines', where_clause="1=1")

print('shp_path: {}'.format(shp_path))
arcpy.Project_management('polyline_layer', shp_path, sr)

fc = shp_path
where = 'FID in (0)'
arcpy.MakeFeatureLayer_management(fc, 'projected_polylines', where_clause=where)
with arcpy.da.SearchCursor('projected_polylines',  ["OID@", "SHAPE@"]) as cursor:
    for row in cursor:
        polyline = row[1]

print(polyline.JSON)


print('')
print(polygon.JSON)
cut_polys = polygon.cut(polyline)
print('after cutting:')

for poly in cut_polys:
    print(poly.JSON)

basepath = os.path.dirname(os.path.abspath(__file__))
shp_path = basepath + r'\cutPoly'

# if the file geodatabase exists, delete it
if os.path.exists(shp_path):
    shutil.rmtree(shp_path)

os.mkdir(shp_path)

# spatial_ref = arcpy.SpatialReference(3857) # WGS 1984
spatial_ref = cut_polys[0].spatialReference

# create a new feature class
arcpy.CreateFeatureclass_management(out_path=shp_path, out_name='cutPoly', geometry_type='POLYGON', template=None, has_m='DISABLED', has_z='DISABLED', spatial_reference=spatial_ref)

arcpy.env.workspace = shp_path

# add attributes to the newly created feature class
# NOTE: OBJECTID is added for you
arcpy.AddField_management('cutPoly.shp', 'Info', 'TEXT', field_alias='Info', field_is_nullable='NULLABLE')

fc = shp_path + r'\cutPoly.shp'

fields = [
    'SHAPE@'
]

polygon.cut(polyline)

with arcpy.da.InsertCursor(fc, fields) as cursor:
    for poly in cut_polys:
        insert = [poly]
        cursor.insertRow(insert)