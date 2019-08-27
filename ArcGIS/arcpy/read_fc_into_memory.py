import csv, sys, arcpy

# read authorotative list of address points into memory
address_points_hash = {}
fc = r'\\server\Administrative\Places'
with arcpy.da.SearchCursor(fc, '*') as cursor:
    for row in cursor:
        objid = row[0]
        address_points_hash[objid] = row

for key in address_points_hash:
    print(address_points_hash[key])
    sys.exit()