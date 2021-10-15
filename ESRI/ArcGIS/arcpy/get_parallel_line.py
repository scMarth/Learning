'''

geodesicDensifyCopyParallelR will create a line parallel to the input line. The other ones give bad results due to distortion from 2D spatial reference

'''

import arcpy, json, decimal

fc = r"D:\TEST_CONNECTONI\TEST.sde\LINES"
where = "OBJECTID IN (1684)"

arcpy.MakeFeatureLayer_management(fc, 'test_layer', where_clause=where)

input_line = None
input_dist = 2 # distance in geodesic

with arcpy.da.SearchCursor('test_layer',  ["OID@", "SHAPE@"]) as cursor:

    for row in cursor:
        # print(row)
        print('OBJECTID: {}'.format(row[0]))
        print('SHAPE: {}'.format(row[1]))

        input_line = row[1]

        print('len geodesic: {}'.format(input_line.getLength("GEODESIC", "METERS")))


        print('json data:')
        json_data = json.loads(row[1].JSON)
        print(json.dumps(json_data, indent=4))
        print('')

print('')

def CopyParallelR(plyP,sLength):
    # sr = arcpy.SpatialReference(3857)
    sr = arcpy.SpatialReference(4326)
    part=plyP.getPart(0)
    rArray=arcpy.Array()
    for ptX in part:
        dL=plyP.measureOnLine(ptX)
        ptX0=plyP.positionAlongLine (dL-0.01).firstPoint
        ptX1=plyP.positionAlongLine (dL+0.01).firstPoint
        dX=float(ptX1.X)-float(ptX0.X)
        dY=float(ptX1.Y)-float(ptX0.Y)
        lenV=math.hypot(dX,dY)
        sX=-dY*sLength/lenV;sY=dX*sLength/lenV
        rightP=arcpy.Point(ptX.X-sX, ptX.Y-sY)
        rArray.add(rightP)
    array = arcpy.Array([rArray])
    section=arcpy.Polyline(array, sr)
    return section


def getDistLine(line):
    part = line.getPart(0)
    first_point = part[0]
    x_fp = first_point.X
    y_fp = first_point.Y
    print(x_fp)
    print(y_fp)
    
    

    sr = arcpy.SpatialReference(4326) # same as input line

    arr = arcpy.Array()
    arr.add(first_point)
    arr.add(
        arcpy.Point(x_fp + 1, y_fp)
    )

    '''

    1 => 2.159093 meters between top points in line, supposed to be 2 meters
    .159093 meters => about 0.52195866142 feet = 6.263503937 inches

    '''

    temp_line = arcpy.Polyline(arr, sr)
    geodesic_dist = temp_line.getLength("GEODESIC", "METERS")
    print('geodesic_dist: {}'.format(geodesic_dist))

    scaled_dist = (input_dist * 1)/geodesic_dist

    parallel_line = CopyParallelR(input_line, scaled_dist)

    with arcpy.da.InsertCursor(fc, ["SHAPE@"]) as cursor:
        insert = [parallel_line]
        cursor.insertRow(insert)


def getDistLineDecimal(line):
    part = line.getPart(0)
    first_point = part[0]
    x_fp = first_point.X
    y_fp = first_point.Y
    print(x_fp)
    print(y_fp)
    
    sr = arcpy.SpatialReference(4326) # same as input line

    arr = arcpy.Array()
    arr.add(first_point)
    arr.add(
        arcpy.Point(x_fp + 1, y_fp)
    )

    '''

    1 => 2.159093 meters between top points in line, supposed to be 2 meters
    .159093 meters => about 0.52195866142 feet = 6.263503937 inches

    same result if decimal is used.

    '''

    temp_line = arcpy.Polyline(arr, sr)
    geodesic_dist = temp_line.getLength("GEODESIC", "METERS")
    print('geodesic_dist: {}'.format(geodesic_dist))

    decimal.getcontext().prec = 40
    scaled_dist = (decimal.Decimal(input_dist) * decimal.Decimal(1))/decimal.Decimal(geodesic_dist)

    parallel_line = CopyParallelR(input_line, float(scaled_dist))
    # parallel_line = CopyParallelR(input_line, float(input_dist))

    with arcpy.da.InsertCursor(fc, ["SHAPE@"]) as cursor:
        insert = [parallel_line]
        cursor.insertRow(insert)

# assume that the input dist is 2 meters (planar)... 
# create a line that is 2 planar meters away from the input line
def planarCopyParallelR(plyP):
    sr4326 = arcpy.SpatialReference(4326)
    sr3857 = arcpy.SpatialReference(3857)

    plyP = plyP.projectAs(sr3857)
    sLength = input_dist

    # sr = arcpy.SpatialReference(3857)
    sr = arcpy.SpatialReference(3857)
    part=plyP.getPart(0)
    rArray=arcpy.Array()
    for ptX in part:
        dL=plyP.measureOnLine(ptX)
        print('ptX.X: {}'.format(ptX.X))
        print('ptX.Y: {}'.format(ptX.Y))
        print('dL: {}'.format(dL))

        ptX0=plyP.positionAlongLine(dL-0.01).firstPoint
        ptX1=plyP.positionAlongLine(dL+0.01).firstPoint

        print('plyP.positionAlongLine(dL-0.01).firstPoint.X: {}'.format(plyP.positionAlongLine(dL-0.01).firstPoint.X))
        print('plyP.positionAlongLine(dL-0.01).firstPoint.Y: {}'.format(plyP.positionAlongLine(dL-0.01).firstPoint.Y))

        print('plyP.positionAlongLine(dL-0.01).JSON: {}'.format(plyP.positionAlongLine(dL-0.01).JSON))
        print('plyP.positionAlongLine(dL-0.01).x: {}'.format(plyP.positionAlongLine(dL-0.01).x))
        print('plyP.positionAlongLine(dL-0.01).y: {}'.format(plyP.positionAlongLine(dL-0.01).y))

        dX=float(ptX1.X)-float(ptX0.X)
        dY=float(ptX1.Y)-float(ptX0.Y)
        lenV=math.hypot(dX,dY)
        sX=-dY*sLength/lenV;sY=dX*sLength/lenV
        rightP=arcpy.Point(ptX.X-sX, ptX.Y-sY)
        rArray.add(rightP)
    array = arcpy.Array([rArray])
    section=arcpy.Polyline(array, sr)


    part_1 = plyP.getPart(0)
    point_1 = part_1[0]
    x_1 = point_1.X
    y_1 = point_1.Y

    part_2 = section.getPart(0)
    point_2 = part_2[0]
    x_2 = point_2.X
    y_2 = point_2.Y

    measureDistArr = arcpy.Array()
    measureDistArr.add(arcpy.Point(x_1, y_1))
    measureDistArr.add(arcpy.Point(x_2, y_2))

    measureLine = arcpy.Polyline(measureDistArr, sr)
    measured = measureLine.getLength("PLANAR", "METERS")
    print('measured: {}'.format(measured))

'''
    with arcpy.da.InsertCursor(fc, ["SHAPE@"]) as cursor:
        insert = [section.projectAs(sr4326)]
        cursor.insertRow(insert)
'''


def geodesicCopyParallelR(input_line, distance):
    sr4326 = arcpy.SpatialReference(4326)

    part = input_line.getPart(0)
    rArray = arcpy.Array()
    for ptX in part:

        dL = input_line.measureOnLine(ptX)
        ptX1 = input_line.positionAlongLine(dL+0.01).firstPoint


        
        print('ptX.X: {}'.format(ptX.X))
        print('ptX.Y: {}'.format(ptX.Y))

        point = arcpy.Point()
        point.X = ptX.X
        point.Y = ptX.Y
        # ptXGeom = arcpy.PointGeometry(inputs=point, spatial_reference=sr4326)
        ptXGeom = arcpy.PointGeometry(point, sr4326)

        angle, dist = ptXGeom.angleAndDistanceTo(ptX1)

        newPoint = ptXGeom.pointFromAngleAndDistance(angle + 90, distance, 'GEODESIC')
        rArray.add(newPoint.firstPoint)
    
    array = arcpy.Array([rArray])
    section = arcpy.Polyline(array, sr4326)


    part_1 = input_line.getPart(0)
    point_1 = part_1[0]
    x_1 = point_1.X
    y_1 = point_1.Y

    part_2 = section.getPart(0)
    point_2 = part_2[0]
    x_2 = point_2.X
    y_2 = point_2.Y

    measureDistArr = arcpy.Array()
    measureDistArr.add(arcpy.Point(x_1, y_1))
    measureDistArr.add(arcpy.Point(x_2, y_2))

    measureLine = arcpy.Polyline(measureDistArr, sr4326)
    measured = measureLine.getLength("GEODESIC", "METERS")
    print('geodesicCopyParallelR measured: {}'.format(measured))

    with arcpy.da.InsertCursor(fc, ["SHAPE@"]) as cursor:
        insert = [section]
        cursor.insertRow(insert)


def geodesicDensifyCopyParallelR(input_line, distance):
    sr4326 = arcpy.SpatialReference(4326)

    print('before:')
    print(input_line.JSON)

    in_mem_fc = r'in_memory\input_line'

    if arcpy.Exists(in_mem_fc):
        arcpy.Delete_management(in_mem_fc)
    
    # create the in memory feature layer for densify
    arcpy.CreateFeatureclass_management(out_path='in_memory', out_name='input_line', geometry_type='POLYLINE', template=None, has_m='DISABLED', has_z='DISABLED', spatial_reference=sr4326)

    with arcpy.da.InsertCursor(in_mem_fc, ['SHAPE@']) as cursor:
        insert = [input_line]
        cursor.insertRow(insert)
    
    # densify the line
    arcpy.Densify_edit(in_mem_fc, "DISTANCE", "5 Feet")

    # get the densified line
    with arcpy.da.SearchCursor(in_mem_fc, ['SHAPE@']) as cursor:
        for row in cursor:
            input_line = row[0]

    print('after:')
    print(input_line.JSON)

    part = input_line.getPart(0)
    rArray = arcpy.Array()
    for ptX in part:

        dL = input_line.measureOnLine(ptX)
        ptX1 = input_line.positionAlongLine(dL+0.01).firstPoint


        
        print('ptX.X: {}'.format(ptX.X))
        print('ptX.Y: {}'.format(ptX.Y))

        point = arcpy.Point()
        point.X = ptX.X
        point.Y = ptX.Y
        # ptXGeom = arcpy.PointGeometry(inputs=point, spatial_reference=sr4326)
        ptXGeom = arcpy.PointGeometry(point, sr4326)

        angle, dist = ptXGeom.angleAndDistanceTo(ptX1)

        newPoint = ptXGeom.pointFromAngleAndDistance(angle + 90, distance, 'GEODESIC')
        rArray.add(newPoint.firstPoint)
    
    array = arcpy.Array([rArray])
    section = arcpy.Polyline(array, sr4326)


    part_1 = input_line.getPart(0)
    point_1 = part_1[0]
    x_1 = point_1.X
    y_1 = point_1.Y

    part_2 = section.getPart(0)
    point_2 = part_2[0]
    x_2 = point_2.X
    y_2 = point_2.Y

    measureDistArr = arcpy.Array()
    measureDistArr.add(arcpy.Point(x_1, y_1))
    measureDistArr.add(arcpy.Point(x_2, y_2))

    measureLine = arcpy.Polyline(measureDistArr, sr4326)
    measured = measureLine.getLength("GEODESIC", "METERS")
    print('geodesicCopyParallelR measured: {}'.format(measured))

    with arcpy.da.InsertCursor(fc, ["SHAPE@"]) as cursor:
        insert = [section]
        cursor.insertRow(insert)


geodesicDensifyCopyParallelR(input_line, input_dist)


'''
# A list of coordinate pairs
#
pointList = [[1,2],[3,5],[7,3]]

# Create an empty Point object
#
point = arcpy.Point()

# A list to hold the PointGeometry objects
#
pointGeometryList = []

# For each coordinate pair, populate the Point object and create
#  a new PointGeometry
for pt in pointList:
    point.X = pt[0]
    point.Y = pt[1]

    pointGeometry = arcpy.PointGeometry(point)
    pointGeometryList.append(pointGeometry)

print('sanity check')
'''
