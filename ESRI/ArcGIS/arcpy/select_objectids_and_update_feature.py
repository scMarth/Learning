import arcpy, json

fc = r"D:\TEST_CONNECTION\TEST.sde\LINES"

where = "OBJECTID in (1467)"

arcpy.MakeFeatureLayer_management(fc, 'test_layer', where_clause=where)

with arcpy.da.UpdateCursor('test_layer', ['SHAPE@', 'NOTES']) as cursor:
    for row in cursor:
        row[1] = 'testing UpdateCursor'
        cursor.updateRow(row)