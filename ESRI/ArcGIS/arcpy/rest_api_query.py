import arcpy, re, os, datetime, sys, requests
from arcpy import env

dataParams = { \
    'f' : 'pjson', \
    'objectIds' : '1', \
    'geometryType' : 'esriGeometryPolyline', \
    'spatialRel' : 'esriSpatialRelIntersects', \
    'outFields' : '*', \
    'returnGeometry' : 'true', \
    'returnTrueCurves' : 'false', \
    'returnIdsOnly' : 'false', \
    'returnCountOnly' : 'false', \
    'returnZ' : 'false', \
    'returnM' : 'false', \
    'returnDistinctValues' : 'false' \
}

p = requests.post('https://test.com/arcgis/rest/services/Services/Example/MapServer/0/query', data=dataParams)

print(p.text)
