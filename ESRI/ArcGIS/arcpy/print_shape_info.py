import arcpy, json

fc = r'C:\Users\test-user\Documents\SCRAPWORK\testPoints\testPoints.shp'

# where = "OBJECTID IN (7840887)"
where = '1=1'

arcpy.MakeFeatureLayer_management(fc, 'test_layer', where_clause=where)

with arcpy.da.SearchCursor('test_layer',  ["OID@", "SHAPE@"]) as cursor:

    for row in cursor:
        print(row[0])
        print(row[1].type)
        json_data = json.loads(row[1].JSON)

        print(json.dumps(json_data, indent=4))
        print('')


