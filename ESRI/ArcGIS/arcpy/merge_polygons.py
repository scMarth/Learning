'''

Notes:

http://resources.esri.com/help/9.3/arcgisengine/java/gp_toolref/data_management_tools/dissolve_data_management_.htm

Polygons that are adjacent i.e. polygons that were cut using a Polygon.cut(polyline) will be merged into one. By default, they will be multi-part. So if you have two adjacent polygons and one polygon further away from the others, the result will be one polygon: one exterior ring for the far away polygon, and another exterior ring for the polygons that are adjacent

'''


import arcpy, sys, os, shutil

def print_to_file(input_str):
    basepath =  os.path.dirname(os.path.abspath(__file__))
    file_path = basepath + r'\output.txt'
    with open(file_path, 'a') as f:
        f.write(input_str + '\n')
        print(input_str)

connection = r"D:\DatabaseConnection\TEST.sde\TEST.AWS."

view = 'BLOCKS_V'
target_layer = connection + view

basepath =  os.path.dirname(os.path.abspath(__file__))

output_text = basepath + r'\output.txt'

# delete output file if it exists
if os.path.exists(output_text):
    os.remove(output_text)

where = "OBJECTID IN (1601,1602,1603,1604,1605)"
# where = "OBJECTID IN (7857128, 7857129)" # intersecting polygons

arcpy.MakeFeatureLayer_management(target_layer, 'test_layer', where_clause=where)

shp_path = basepath + r'\multiPartPoly'

# if the file geodatabase exists, delete it
if os.path.exists(shp_path):
    shutil.rmtree(shp_path)

os.mkdir(shp_path)


# arcpy.Union_analysis("test_layer", shp_path) # this will result in many polygon records

# arcpy.Merge_management("test_layer", shp_path + r'\testMultiPartPoly') # will just contain the polygons from the input

# arcpy.Dissolve_management("test_layer", shp_path + r'\coverage', "TRANSACTIONAL_RANCH_NUMBER") # works
# arcpy.Dissolve_management("test_layer", r"in_memory\out_layer", "TRANSACTIONAL_RANCH_NUMBER") # in memory
arcpy.Dissolve_management("test_layer", r"in_memory\out_layer") # in memory, i think this will just dissolve all without field

with arcpy.da.SearchCursor(r'in_memory\out_layer', ['SHAPE@']) as cursor:
    for row in cursor:
        multiPartPolygon = row[0]

        print('MULTI PART POLYGON:')
        print('JSON:\n{}'.format(multiPartPolygon.JSON))
        print('isMultipart: {}'.format(multiPartPolygon.isMultipart))
        print('partCount: {}'.format(multiPartPolygon.partCount))
        print('spatialReference: {}'.format(multiPartPolygon.spatialReference))
        print('getPart: {}'.format(multiPartPolygon.getPart()))

arcpy.FeatureClassToShapefile_conversion(r'in_memory\out_layer', shp_path)
arcpy.Delete_management("in_memory")


