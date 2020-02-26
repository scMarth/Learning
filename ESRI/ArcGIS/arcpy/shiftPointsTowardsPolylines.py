import arcpy
import sys
import datetime

# returns the coordinates of point (Cx, Cy) orthogonally projected onto line AB,
# where AB is given by coordinates (Ax, Ay) and (Bx, By)
def orthogonallyProjectPointToLine(Ax, Ay, Bx, By, Cx, Cy):
    Ax = float(Ax)
    Ay = float(Ay)
    Bx = float(Bx)
    By = float(By)
    Cx = float(Cx)
    Cy = float(Cy)

    # find the slope from A to B
    m = (Ay-By)/(Ax-Bx)

    # solve for b in the equation y = mx + b
    b = Ay - m * Ax

    # find slope orthogonal to line AB
    mp = -1 / m

    # solve for b in the equation y = mpx + bp
    bp = Cy + (1/m)*Cx

    # find an x coordinate of point C orthogonally projected onto line AB
    xp = (Ay - m*Ax - Cy + mp*Cx)/(mp-m)

    # find the y coordinate of point C orthongonally projected onto line AB
    yp = m*xp + Ay - m*Ax # (using equation for line AB)

    return [xp, yp]

def getPointCoords(objectId):
    selectedPoint = arcpy.SelectLayerByAttribute_management("PointsTemp", "NEW_SELECTION", "OBJECTID = {}".format(objectId))
    with arcpy.da.SearchCursor(selectedPoint, ['OID@', 'SHAPE@XY']) as cursor:
        for row in cursor:
            point = row[1]
            return [point[0], point[1]]

def getCenterlineCoords(objectId):
    coordsArray = []
    centerline = arcpy.SelectLayerByAttribute_management("CenterlineTemp", "NEW_SELECTION", "OBJECTID = {}".format(objectId))
    with arcpy.da.SearchCursor(centerline, ['OID@', 'SHAPE@']) as cursor:
        for row in cursor:
            polyline = row[1]
            for line in polyline:
                for point in line:
                    if point:
                        coordsArray.append((point.X, point.Y))
    return coordsArray


# find the distance beteen points (Ax, Ay) and (Bx, By)
def getDistanceBetweenPoints(Ax, Ay, Bx, By):
    Ax = float(Ax)
    Ay = float(Ay)
    Bx = float(Bx)
    By = float(By)

    distance = ((Ax-Bx)**2 + (Ay-By)**2)**(float(1)/2)
    return distance

# decrease distance between point (Ax, Ay) and (Bx, By), where point B 
# is the projcted point. Return a new value A' s.t. A' is closer to 
# point B than point A
def decreaseDistance(Ax, Ay, Bx, By):
    Ax = float(Ax)
    Ay = float(Ay)
    Bx = float(Bx)
    By = float(By)

    # find the slope from A to B
    m = (Ay-By)/(Ax-Bx)

    # solve for b in the equation y = mx + b
    b = Ay - m * Ax

    dist = getDistanceBetweenPoints(Ax, Ay, Bx, By)

    AxPrime = None

    if Bx < Ax: # decrease x-coordinate by 1
        AxPrime = Ax - float(1)
    elif Bx > Ax: # increase x-coordinate by 1
        AxPrime = Ax + float(1)
    else:
        sys.stderr.write("decreaseDistance: Ax = Bx ; Aborting.")
        sys.exit()

    AyPrime = float(m)*AxPrime + b
    return [AxPrime, AyPrime]

'''

Given a point and a projection point (both are arrays of size 2 where
the first value is the x-coordinate and the second is the y-coordinate),
create a copy of the point and then shift the copy until it is no longer
inside any parcel

'''
def shiftPointTowardsProjectionUntilOutside(pointCoords, projectionCoords):
    global spatial_reference

    # select all parcels
    allParcels = arcpy.SelectLayerByAttribute_management("ParcelJoinTemp", "NEW_SELECTION")    

    point = arcpy.PointGeometry(arcpy.Point(pointCoords[0],pointCoords[1]), spatial_reference)

    # select the parcel that contains that point
    parcelThatContainsPoint = arcpy.SelectLayerByLocation_management(allParcels, overlap_type = 'CONTAINS', select_features = point, selection_type = "NEW_SELECTION")

    # count the number of parcels that contains the point (either 1 or 0)
    numParcelsThatContainPoint = 0
    with arcpy.da.SearchCursor(parcelThatContainsPoint, '*') as cursor:
        for row in cursor:
            numParcelsThatContainPoint += 1

    shiftingPoint = pointCoords

    # move the point until no more parcels contain it
    while (numParcelsThatContainPoint != 0):

        shiftingPoint = decreaseDistance(shiftingPoint[0], shiftingPoint[1], projectionCoords[0], projectionCoords[1]) # decrease distance to projected point
        point = arcpy.PointGeometry(arcpy.Point(shiftingPoint[0],shiftingPoint[1]), spatial_reference)
        parcelThatContainsPoint = arcpy.SelectLayerByLocation_management(allParcels, overlap_type = 'CONTAINS', select_features = point, selection_type = "NEW_SELECTION")

        numParcelsThatContainPoint = 0
        with arcpy.da.SearchCursor(parcelThatContainsPoint, '*') as cursor:
            for row in cursor:
                numParcelsThatContainPoint += 1

    return shiftingPoint

'''
Given an Object ID of a point and an Object ID of the corresponding centerline, do the following:

    1.) Find the closest line in the centerline's polyline shape to the point
    2.) Project the point to that line
    3.) Shift a point from the point towards the projected point until the point is outside the respective parcel
    4.) Return the coordinates of the shifted point

'''
def movePointTowardsCenterline(pointId, centerlineId):
    global spatial_reference

    # get the coordinates of the centerline
    coordsArray = getCenterlineCoords(centerlineId)

    # get the coordinates of the point
    pointCoords = getPointCoords(pointId)

    minimumDistance = None
    minimumIndex = None # index of the line within the polyline

    # find the closest line in the polyline to the point

    for i in range(0, len(coordsArray)-1):
        Ax = coordsArray[i][0]
        Ay = coordsArray[i][1]
        Bx = coordsArray[i+1][0]
        By = coordsArray[i+1][1]

        dist1 = getDistanceBetweenPoints(pointCoords[0], pointCoords[1], Ax, Ay)
        dist2 = getDistanceBetweenPoints(pointCoords[0], pointCoords[1], Bx, By)

        avgDist = dist1 + dist2 / float(2)

        # keep track of the running minimum
        if minimumDistance is None or avgDist < minimumDistance:
            minimumDistance = avgDist
            minimumIndex = i

    # get the coordinates of the point projected onto the line we just found
    projectionCoords = orthogonallyProjectPointToLine( \
                            coordsArray[minimumIndex][0], \
                            coordsArray[minimumIndex][1], \
                            coordsArray[minimumIndex+1][0], \
                            coordsArray[minimumIndex+1][1], \
                            pointCoords[0], \
                            pointCoords[1])

    shiftedPoint = shiftPointTowardsProjectionUntilOutside(pointCoords, projectionCoords)

    # return projectionCoords
    return shiftedPoint

# Set variables for GDB layers
path = r'scratch.gdb'
arcpy.env.workspace = path
places = "PointsSample"
streets = "RoadwayCenterlines"
parcels_lines= "Parcel_to_line"
parcels = "ParcelsSample"

print(datetime.datetime.now())
print("")

# create temporary virtual datasets for RoadwayCenterlines and PointsSample to be used with functions
arcpy.MakeFeatureLayer_management("RoadwayCenterlines", "CenterlineTemp")
arcpy.MakeFeatureLayer_management("PointsSample", "PointsTemp")
arcpy.MakeFeatureLayer_management("ParcelsSample", "singleParcelTemp")

# if a feature class called 'ShiftedPoints' exists, delete it so that it can be remade
if arcpy.Exists(path + r'\ShiftedPoints'):
    arcpy.Delete_management(path + r'\ShiftedPoints')

out_path = path
out_name = "ShiftedPoints"
geometry_type = "POINT"
template = None
has_m = "DISABLED"
has_z = "DISABLED"

# use same spatial reference as Roadway_Centerlines
spatial_reference = arcpy.Describe(path + r'\RoadwayCenterlines').spatialReference
# create a new feature class
arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template, has_m, has_z, spatial_reference)

# add attributes to the newly created feature clas (should have same attributes as PointsSample)
arcpy.AddField_management("ShiftedPoints", "PointsSample_ObjId", "TEXT", field_alias="PointsSample Object ID", field_is_nullable="NON_NULLABLE")
arcpy.AddField_management("ShiftedPoints", "CountyFID", "LONG", field_alias="CountyFID", field_is_nullable="NULLABLE")
arcpy.AddField_management("ShiftedPoints", "CountyOID", "LONG", field_alias="CountyOID", field_is_nullable="NULLABLE")
arcpy.AddField_management("ShiftedPoints", "USE_TYPE", "TEXT", field_alias="USE_TYPE", field_is_nullable="NULLABLE", field_length=80)
arcpy.AddField_management("ShiftedPoints", "SPECIFIC_U", "TEXT", field_alias="SPECIFIC_U", field_is_nullable="NULLABLE", field_length=80)
arcpy.AddField_management("ShiftedPoints", "NAME", "TEXT", field_alias="NAME", field_is_nullable="NULLABLE", field_length=80)
arcpy.AddField_management("ShiftedPoints", "SUBNAME", "TEXT", field_alias="SUBNAME", field_is_nullable="NULLABLE", field_length=80)
arcpy.AddField_management("ShiftedPoints", "NUMBER_", "TEXT", field_alias="NUMBER_", field_is_nullable="NULLABLE", field_length=80)
arcpy.AddField_management("ShiftedPoints", "PREFIX", "TEXT", field_alias="PREFIX", field_is_nullable="NULLABLE", field_length=80)
arcpy.AddField_management("ShiftedPoints", "STREET", "TEXT", field_alias="STREET", field_is_nullable="NULLABLE", field_length=80)
arcpy.AddField_management("ShiftedPoints", "STREET_ALI", "TEXT", field_alias="STREET_ALI", field_is_nullable="NULLABLE", field_length=80)
arcpy.AddField_management("ShiftedPoints", "SUFFIX", "TEXT", field_alias="SUFFIX", field_is_nullable="NULLABLE", field_length=80)
arcpy.AddField_management("ShiftedPoints", "SUITE", "TEXT", field_alias="SUITE", field_is_nullable="NULLABLE", field_length=80)
arcpy.AddField_management("ShiftedPoints", "ZIP", "TEXT", field_alias="ZIP", field_is_nullable="NULLABLE", field_length=80)
arcpy.AddField_management("ShiftedPoints", "ADDRESS_FU", "TEXT", field_alias="ADDRESS_FU", field_is_nullable="NULLABLE", field_length=80)
arcpy.AddField_management("ShiftedPoints", "CMNTY_CODE", "TEXT", field_alias="CMNTY_CODE", field_is_nullable="NULLABLE", field_length=80)
arcpy.AddField_management("ShiftedPoints", "CITY", "TEXT", field_alias="CITY", field_is_nullable="NULLABLE", field_length=80)
arcpy.AddField_management("ShiftedPoints", "X", "DOUBLE", field_alias="X", field_is_nullable="NULLABLE", field_precision=0, field_scale=0)

# Make a temporary virtual dataset for the parcels layer
arcpy.MakeFeatureLayer_management(parcels, "ParcelJoinTemp")
arcpy.MakeFeatureLayer_management(streets, "RoadTemp")
# Select all parcels with a join count equal to one
SingleAdd = arcpy.SelectLayerByAttribute_management("ParcelJoinTemp", "NEW_SELECTION", '"Join_Count" = 1' )

# Make a temporary virtual dataset for the Places layer
arcpy.MakeFeatureLayer_management(places, "PlacesTemp")
# Select all places in PointSample that intersect the selected parcels
SingleAddParcel = arcpy.SelectLayerByLocation_management("PlacesTemp", overlap_type = 'WITHIN', select_features = SingleAdd, selection_type = "NEW_SELECTION")

shiftedCoords = []
pointInfo = []

pointsProcessed = 0

# Iteratively select each row from the PlacesTemp layer and apply a search radius, select intersecting streets, and check for matches in the respective street name fields
# with arcpy.da.SearchCursor(SingleAddParcel, ["OBJECTID"]) as cursor:
with arcpy.da.SearchCursor(SingleAddParcel, '*') as cursor:
    for row in cursor:
        pointInfo.append(row)

        arcpy.SelectLayerByAttribute_management(SingleAddParcel, "NEW_SELECTION", "OBJECTID = {}".format(row[0]))
        singleAddParcelSel = [row for row in arcpy.da.SearchCursor(SingleAddParcel, ["OBJECTID", "street"])]
        
        placeValue = singleAddParcelSel[0][1] # placeValue = the 'street' field of the current single address parcel
        singleAddObjId = singleAddParcelSel[0][0] # PointSample?

        radius = 20
        # loop and increase the search radius until a match is found
        while (True):
            
            distance = str(radius) + " feet"
            hasMatch = False
            
            arcpy.SelectLayerByLocation_management("RoadTemp", "WITHIN_A_DISTANCE", SingleAddParcel, distance, "NEW_SELECTION") # ? not sure how this works
            roadTempSelectedRecords = [row for row in arcpy.da.SearchCursor("RoadTemp", ["OBJECTID", "NAME_ALF"])] # select the fields we need
            streetValues = [row[1] for row in roadTempSelectedRecords] # street values in Roadway Centerlines within 'radius' of the parcel

            numberOfMatches = streetValues.count(placeValue)
            if numberOfMatches == 1:
                objectId = roadTempSelectedRecords[streetValues.index(placeValue)][0]

                coords = movePointTowardsCenterline(singleAddObjId, objectId)
                
                shiftedCoords.append(coords)
                break
            elif numberOfMatches > 1:
                print(str(numberOfMatches) + " matches")
                break
            else:
                radius += 5

        pointsProcessed += 1
        print("pointsProcessed: {}".format(pointsProcessed))

# insert the orthogonally projected coordinates into the new feature class
fc = path + r'\ShiftedPoints'
fields = [ \
    "PointsSample_ObjId", \
    "SHAPE@XY", \
    "CountyFID", \
    "CountyOID", \
    "USE_TYPE", \
    "SPECIFIC_U", \
    "NAME", \
    "SUBNAME", \
    "NUMBER_", \
    "PREFIX", \
    "STREET", \
    "STREET_ALI", \
    "SUFFIX", \
    "SUITE", \
    "ZIP", \
    "ADDRESS_FU", \
    "CMNTY_CODE", \
    "CITY", \
    "X" \
]

with arcpy.da.InsertCursor(fc, fields) as cursor:
    for i in range(0, len(shiftedCoords)):
        xy = (shiftedCoords[i][0], shiftedCoords[i][1])

        cursor.insertRow(( \
            pointInfo[i][0], \
            xy, \
            pointInfo[i][2], \
            pointInfo[i][3], \
            pointInfo[i][4], \
            pointInfo[i][5], \
            pointInfo[i][6], \
            pointInfo[i][7], \
            pointInfo[i][8], \
            pointInfo[i][9], \
            pointInfo[i][10], \
            pointInfo[i][11], \
            pointInfo[i][12], \
            pointInfo[i][13], \
            pointInfo[i][14], \
            pointInfo[i][15], \
            pointInfo[i][16], \
            pointInfo[i][17], \
            pointInfo[i][18], \
        ))

print("")
print("Done")
print(datetime.datetime.now())
