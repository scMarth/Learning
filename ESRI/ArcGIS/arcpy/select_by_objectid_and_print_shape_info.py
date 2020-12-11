import arcpy, json

fc = r"D:\TEST_CONNECTION\TEST.sde\LINES"
where = "OBJECTID IN (1684,447)"

arcpy.MakeFeatureLayer_management(fc, 'test_layer', where_clause=where)

with arcpy.da.SearchCursor('test_layer',  ["OID@", "SHAPE@"]) as cursor:

    for row in cursor:
        # print(row)
        print('objectid: ', row[0])
        print(row[1].JSON)
        print('')