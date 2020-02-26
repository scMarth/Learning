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

p = requests.post('https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/CurrentSweeperRoutes/MapServer/0/query', data=dataParams)

print(p.text)

# json_data = json.loads(p.text)


'''
equivalent to query:

https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/CurrentSweeperRoutes/MapServer/0/query?where=&text=&objectIds=1&time=&geometry=&geometryType=esriGeometryPolyline&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&resultOffset=&resultRecordCount=&f=pjson

'''