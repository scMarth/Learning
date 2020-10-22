import arcpy, os, shutil, numpy

def create_test_points():
    basepath = os.path.dirname(os.path.abspath(__file__))
    shp_path = basepath + r'\testPoints'

    # if the file geodatabase exists, delete it
    if os.path.exists(shp_path):
        shutil.rmtree(shp_path)

    os.mkdir(shp_path)

    # create fgdb
    # arcpy.CreateFileGDB_management(basepath, 'testPoints')

    spatial_ref = arcpy.SpatialReference(3857) # WGS 1984

    # create a new feature class
    arcpy.CreateFeatureclass_management(out_path=shp_path, out_name='testPoints', geometry_type='POINT', template=None, has_m='DISABLED', has_z='DISABLED', spatial_reference=spatial_ref)

    arcpy.env.workspace = shp_path

    # add attributes to the newly created feature class
    # NOTE: OBJECTID is added for you
    arcpy.AddField_management('testPoints.shp', 'Info', 'TEXT', field_alias='Info', field_is_nullable='NULLABLE')

    fc = shp_path + r'\testPoints.shp'

    fields = [ \
        'SHAPE@XY', \
        'Info' \
    ]

    coords = [
        [-13538139.7457, 4405781.42109],
        [-13538588.1553, 4405096.70195],
        [-13538042.5644, 4405929.81652],
        [-13538685.3366, 4404948.30651]
    ]

    data = [
        ['pn1'],
        ['pn2'],
        ['p1'],
        ['p2'],
    ]

    with arcpy.da.InsertCursor(fc, fields) as cursor:
        for i in range(len(data)):
            record = data[i]
            
            curr_coords = coords[i]

            xy = (curr_coords[0], curr_coords[1])
            insert = [xy]

            for field in record:
                insert.append(field)

            cursor.insertRow(insert)


def create_test_polygons():
    basepath = os.path.dirname(os.path.abspath(__file__))
    shp_path = basepath + r'\testPolygons'

    # if the file geodatabase exists, delete it
    if os.path.exists(shp_path):
        shutil.rmtree(shp_path)

    os.mkdir(shp_path)

    spatial_ref = arcpy.SpatialReference(4326) # WGS 1984

    # create a new feature class
    arcpy.CreateFeatureclass_management(out_path=shp_path, out_name='testPolygons', geometry_type='POLYGON', template=None, has_m='DISABLED', has_z='DISABLED', spatial_reference=spatial_ref)

    arcpy.env.workspace = shp_path

    # add attributes to the newly created feature class
    # NOTE: OBJECTID is added for you
    arcpy.AddField_management('testPolygons.shp', 'Info', 'TEXT', field_alias='Info', field_is_nullable='NULLABLE')

    fc = shp_path + r'\testPolygons.shp'

    fields = [ \
        'SHAPE@', \
        'Info' \
    ]

    coords_list = [[
        [-121.61775581499995, 36.75887873200003],
        [-121.61692451099998, 36.75840343100003],
        [-121.61738840799995, 36.75783622600005],
        [-121.61820810999996, 36.75828153800006],
        [-121.61775581499995, 36.75887873200003]
    ]]

    data = [
        ['appl block 7840887']
    ]

    with arcpy.da.InsertCursor(fc, fields) as cursor:
        for i in range(len(data)):
            record = data[i]
            
            curr_coords = coords_list[i]

            # note: we are assuming that there is just one ring
            array = []
            for coord in curr_coords:
                # print(coord)
                point = arcpy.Point(coord[0], coord[1])
                # print(point)
                array.append(point)

            # for item in array:
            #     print(item)

            rings = arcpy.Array(array)


            # print("rings")
            # for item in rings:
            #     print(rings)

            polygon = arcpy.Polygon(rings, spatial_ref)
            # print(polygon.JSON)

            insert = [polygon]

            for field in record:
                insert.append(field)

            cursor.insertRow(insert)

    with arcpy.da.SearchCursor(fc, fields) as cursor:
        for row in cursor:
            print(row)



def create_test_polylines():
    basepath = os.path.dirname(os.path.abspath(__file__))
    shp_path = basepath + r'\testPolylines'

    # if the file geodatabase exists, delete it
    if os.path.exists(shp_path):
        shutil.rmtree(shp_path)

    os.mkdir(shp_path)

    spatial_ref = arcpy.SpatialReference(3857) # WGS 1984

    # create a new feature class
    arcpy.CreateFeatureclass_management(out_path=shp_path, out_name='testPolylines', geometry_type='POLYLINE', template=None, has_m='DISABLED', has_z='DISABLED', spatial_reference=spatial_ref)

    arcpy.env.workspace = shp_path

    # add attributes to the newly created feature class
    # NOTE: OBJECTID is added for you
    arcpy.AddField_management('testPolylines.shp', 'Info', 'TEXT', field_alias='Info', field_is_nullable='NULLABLE')

    fc = shp_path + r'\testPolylines.shp'

    fields = [ \
        'SHAPE@', \
        'Info' \
    ]

    coords_list = [
        [
            [-13538334.108408503, 4405484.630223595],
            [-13538396.195396204, 4405389.901372597]
        ],
        [
            [-13538334.108416803, 4405484.630210996],
            [-13538385.758454002, 4405405.825475]
        ]
    ]

    data = [
        ['867 before running the script'],
        ['867 after running the waylines script']
    ]

    with arcpy.da.InsertCursor(fc, fields) as cursor:
        for i in range(len(data)):
            record = data[i]
            
            curr_coords = coords_list[i]

            # note: we are assuming that there is just one ring
            array = arcpy.Array()
            for coord in curr_coords:
                # print(coord)
                point = arcpy.Point(coord[0], coord[1])
                # print(point)
                array.add(point)

            polyline = arcpy.Polyline(array, spatial_ref)
            print(polyline.JSON)

            insert = [polyline]

            for field in record:
                insert.append(field)

            cursor.insertRow(insert)

    with arcpy.da.SearchCursor(fc, fields) as cursor:
        for row in cursor:
            print(row)

create_test_points()
create_test_polygons()
create_test_polylines()
print('Done.')