import arcpy, json, os, shutil




workspace = os.path.dirname(os.path.abspath(__file__))
geojson_path = workspace + r'\test_output.geojson'
# geojson_path = workspace + r'\test_output2.geojson'

spatial_ref_wgs84 = arcpy.SpatialReference(4326)

shp_path = workspace + r'\microclimates'

if os.path.exists(shp_path):
    shutil.rmtree(shp_path)
os.mkdir(shp_path)

# create output shapefile
arcpy.management.CreateFeatureclass(
    out_path = shp_path,
    out_name = 'microclimates',
    geometry_type = 'POLYGON',
    spatial_reference=spatial_ref_wgs84
)

arcpy.management.AddField(
    in_table = shp_path + r'\microclimates.shp',
    field_name = 'name',
    field_type = 'TEXT',
    field_length = 100
)



with arcpy.da.InsertCursor(shp_path + r'\microclimates.shp', ['SHAPE@','name']) as ic:


    with open(geojson_path, 'r') as file:
        data = json.load(file)

        for feature in data['features']:
            name = feature['properties']['Name']
            geometry = feature['geometry']
            number_of_rings = len(geometry['coordinates'])
            polygon_type = feature['geometry']['type']



            polygon_data = {
                "rings" : geometry['coordinates'],
                "spatialReference":
                    {
                        "wkid" : 3857,
                        "latestWkid" : 3857
                    }
            }

            spatial_ref = arcpy.SpatialReference(polygon_data['spatialReference']['wkid'])

            print(name)
            print('number of rings: {}'.format(number_of_rings))
            print('')

            if polygon_type == 'Polygon':


                # note: we are assuming that there is just one ring
                array = []
                for coord in polygon_data['rings'][0]:
                    point = arcpy.Point(coord[0], coord[1])
                    array.append(point)

                rings = arcpy.Array(array)

                polygon = arcpy.Polygon(rings, spatial_ref)
                ic.insertRow([polygon, name])


                continue

            else:

                single_polygons = []
                for ring in geometry['coordinates']:
                    # assume single array
                    coords = ring[0]
                    array = []

                    for coord in coords:
                        # print(coord)
                        point = arcpy.Point(coord[0], coord[1])
                        array.append(point)
                    
                    rings = arcpy.Array(array)
                    polygon = arcpy.Polygon(rings, spatial_ref)
                    single_polygons.append(polygon)
                
                print(single_polygons)

                merged_polygon = None

                # combine multi polygons:
                if len(single_polygons) > 1:
                    combined_array = arcpy.Array()

                    for poly in single_polygons:
                        for part in poly.getPart():
                            combined_array.add(part)

                    merged_polygon = arcpy.Polygon(combined_array, spatial_ref)

                else:
                    merged_polygon = single_polygons[0]

                # change to wgs 84
                merged_polygon = merged_polygon.projectAs(spatial_ref_wgs84)

                ic.insertRow([merged_polygon, name])








sys.exit()
