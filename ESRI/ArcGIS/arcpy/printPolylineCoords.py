import arcpy
import sys

def printCenterlineCoords(objectId):
    arcpy.MakeFeatureLayer_management("RoadwayCenterlines", "CenterlineTemp")
    centerline = arcpy.SelectLayerByAttribute_management("CenterlineTemp", "NEW_SELECTION", "OBJECTID = {}".format(objectId))
    with arcpy.da.SearchCursor(centerline, ['OID@', 'SHAPE@']) as cursor:
        for row in cursor:
            polyline = row[1]
            for line in polyline:
                for point in line:
                    if point:
                        print("{}, {}".format(point.X, point.Y))

arcpy.env.workspace = r'scratch.gdb'

# Set variables for GDB layers
path = r'scratch.gdb'
places = "PointsSample"
streets = "RoadwayCenterlines"
parcels_lines= "Parcel_to_line"
parcels = "ParcelsSample"

# Make a temporary virtual dataset for the parcels layer
arcpy.MakeFeatureLayer_management(parcels, "ParcelJoinTemp")
arcpy.MakeFeatureLayer_management(streets, "RoadTemp")
# Select all parcels with a join count equal to one
SingleAdd = arcpy.SelectLayerByAttribute_management("ParcelJoinTemp", "NEW_SELECTION", '"Join_Count" = 1' )

# Make a temporary virtual dataset for the Places layer
arcpy.MakeFeatureLayer_management(places, "PlacesTemp")
# Select all places in PointSample that intersect the selected parcels
SingleAddParcel = arcpy.SelectLayerByLocation_management("PlacesTemp", overlap_type = 'WITHIN', select_features = SingleAdd, selection_type = "NEW_SELECTION")

# Iteratively select each row from the PlacesTemp layer and apply a search radius, select intersecting streets, and check for matches in the respective street name fields
with arcpy.da.SearchCursor(SingleAddParcel, ["OBJECTID"]) as cursor:
    for row in cursor:
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
                print(singleAddObjId) # object ID in PointSample
                print(objectId) # object ID of corresponding centerlines
                printCenterlineCoords(objectId)

                # findOrthProjCoord()
                # find distance between these two object Ids

                print("")
                break
            elif numberOfMatches > 1:
                print(str(numberOfMatches) + " matches")
                break
            else:
                radius += 5
            
        break;
print("Done")
