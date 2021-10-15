'''

note: this is inaccurate because WGS1984 uses an ellipsoid model:

https://gisgeography.com/wgs84-world-geodetic-system/#:~:text=The%20Global%20Positioning%20System%20uses,mass%20as%20the%20coordinate%20origin.

'''

import arcpy, sys, os, shutil

def print_to_file(input_str):
    basepath =  os.path.dirname(os.path.abspath(__file__))
    file_path = basepath + r'\output.txt'
    with open(file_path, 'a') as f:
        f.write(input_str + '\n')
        print(input_str)

connection = r"D:\Testing\SCRAPWORK.sde\egdb.TEST."

view = 'TEST_POLYS'
target_layer = connection + view

basepath =  os.path.dirname(os.path.abspath(__file__))

output_text = basepath + r'\output.txt'

# delete output file if it exists
if os.path.exists(output_text):
    os.remove(output_text)

where = "OBJECTID IN (254698, 254706, 4340787)"
where = "OBJECTID IN (254706, 4340787)"
where = "OBJECTID IN (214738, 195113, 214740, 254706, 254705, 708875, 708873, 708872, 254706)" # 195113 is the center

arcpy.MakeFeatureLayer_management(target_layer, 'test_layer', where_clause=where)

points_to_dump = []

singlePolyCentroidCoords = []

fid_count = 0
with arcpy.da.SearchCursor('test_layer', ['OID@', 'SHAPE@']) as cursor:
    for row in cursor:
        oid = row[0]
        poly = row[1]

        print('OBJECTID: {}'.format(oid))
        print('shape:')
        print(poly.JSON)
        print('isMultipart: {}'.format(poly.isMultipart))
        print('partCount: {}'.format(poly.partCount))

        centroid = poly.centroid

        xy = [centroid.X, centroid.Y]

        points_to_dump.append([centroid.X, centroid.Y, '{} centroid, partcount: {}, FID = {}'.format(oid, poly.partCount, fid_count)])

        fid_count += 1

        singlePolyCentroidCoords.append(xy)

print(singlePolyCentroidCoords)

# using algorithm from: https://stackoverflow.com/questions/6671183/calculate-the-center-point-of-multiple-latitude-longitude-coordinate-pairs
import math
def deg2rad(degr):
    return (degr * math.pi) / 180

def rad2degr(rad):
    return (rad * 180) / math.pi

def getLongLatCenterCoords(coords):
    sumX = 0.0
    sumY = 0.0
    sumZ = 0.0

    # coords are [x, y]
    for coord in coords:
        long = deg2rad(coord[0]) # long is x
        lat = deg2rad(coord[1]) # lat is y

        print('long: {}, lat: {}'.format(long, lat))

        # sum of cartesian coordinates
        sumX += math.cos(lat) * math.cos(long)
        sumY += math.cos(lat) * math.sin(long)
        sumZ += math.sin(lat)

    avgX = sumX / len(coords)
    avgY = sumY / len(coords)
    avgZ = sumZ / len(coords)

    # convert avg x, y, z coordinates to latitude and longitude

    lng = math.atan2(avgY, avgX)
    hyp = math.sqrt(avgX * avgX + avgY * avgY)
    lat = math.atan2(avgZ, hyp)

    return [rad2degr(lat), rad2degr(lng)]

manualCentroidCalc = getLongLatCenterCoords(singlePolyCentroidCoords)

print('manualCentroidCalc: {}'.format(manualCentroidCalc))


points_to_dump.append(manualCentroidCalc + ['manually calculated with trig'])



# dump individual polygons
shp_path = basepath + r'\individualPolys'
if os.path.exists(shp_path):
    shutil.rmtree(shp_path)
os.mkdir(shp_path)
arcpy.FeatureClassToShapefile_conversion('test_layer', shp_path)





shp_path = basepath + r'\multiPartPoly'

# if the file geodatabase exists, delete it
if os.path.exists(shp_path):
    shutil.rmtree(shp_path)

os.mkdir(shp_path)

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

        centroid = multiPartPolygon.centroid

        print('ArcGIS:\nCentroid X: {}\nCentroid Y: {}'.format(centroid.X, centroid.Y))

        points_to_dump.append([centroid.X, centroid.Y, 'calculated using ArcGIS'])

arcpy.FeatureClassToShapefile_conversion(r'in_memory\out_layer', shp_path)
arcpy.Delete_management("in_memory")





# dump the centroid points computed from both methods

def create_test_points(coord_data):
    basepath = os.path.dirname(os.path.abspath(__file__))
    shp_path = basepath + r'\testPoints'

    # if the file geodatabase exists, delete it
    if os.path.exists(shp_path):
        shutil.rmtree(shp_path)

    os.mkdir(shp_path)

    # create fgdb
    # arcpy.CreateFileGDB_management(basepath, 'testPoints')

    spatial_ref = arcpy.SpatialReference(4326) # WGS 1984

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

    coords = []
    data = []
    for item in coord_data:
        x, y, label = item
        coords.append([x, y])
        data.append([label])

    with arcpy.da.InsertCursor(fc, fields) as cursor:
        for i in range(len(data)):
            record = data[i]
            
            curr_coords = coords[i]

            xy = (curr_coords[0], curr_coords[1])
            insert = [xy]

            for field in record:
                insert.append(field)

            cursor.insertRow(insert)


create_test_points(points_to_dump)