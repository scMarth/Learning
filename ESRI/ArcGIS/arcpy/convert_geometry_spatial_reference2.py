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

def convert_wgs84_to_nad83(longitude, latitude):
    point = arcpy.Point(longitude, latitude)
    sr = arcpy.SpatialReference(4326) # WGS84
    point_geometry = arcpy.PointGeometry(point, sr)

    target_spatial_ref = arcpy.SpatialReference(102644) # NAD83
    projected = point_geometry.projectAs(target_spatial_ref)

    return [projected.firstPoint.X, projected.firstPoint.Y]

longitude = -121.6515268
latitude = 36.6735302

longitude2, latitude2 = convert_wgs84_to_nad83(longitude, latitude)

print('long: {} ; lat: {}'.format(longitude, latitude))
print('long: {} ; lat: {}'.format(longitude2, latitude2))