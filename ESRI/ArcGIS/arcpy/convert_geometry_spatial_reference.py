import arcpy, os, datetime, sys

# Convert a PointGeometry to a different spatial reference given a target coordinate system's factory code (or authority code, or well-known ID (wkid)).
# Returns the resulting PointGeometry
def convert_to_spatial_reference(point_geometry, factory_code):
    if point_geometry.spatialReference.factoryCode != factory_code:
        target_spatial_ref = arcpy.SpatialReference(factory_code)
        point_geometry = point_geometry.projectAs(target_spatial_ref)
        return point_geometry
    else:
        return point_geometry


x = -121.65731271093892 # longitude
y = 36.67526264843514 # latitude
wkid = 4326 # spatial Reference 

point = arcpy.Point(x, y)
sr = arcpy.SpatialReference(wkid)
point_geometry = arcpy.PointGeometry(point, sr)

print("Before:")
print("\t" + str(point_geometry))
print("\t" + str(point_geometry.spatialReference.factoryCode))
print("\t" + str(point_geometry.JSON))
print("\t" + str(point_geometry.firstPoint.X))
print("\t" + str(point_geometry.firstPoint.Y))
print("")
print("")

point_geometry = convert_to_spatial_reference(point_geometry, 102644)

print("After:")
print("\t" + str(point_geometry))
print("\t" + str(point_geometry.spatialReference.factoryCode))
print("\t" + str(point_geometry.JSON))
print("\t" + str(point_geometry.firstPoint.X))
print("\t" + str(point_geometry.firstPoint.Y))
print("")

