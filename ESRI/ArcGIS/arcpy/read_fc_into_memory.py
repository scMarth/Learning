import csv, sys, arcpy

# read authorotative list of address points into memory
address_points_hash = {}
fc = r'\\server\Administrative\Places'

field_to_index_map = {}
index_count = 0
fields = arcpy.ListFields(fc)
for field in fields:
    print(field.name)
    field_to_index_map[field.name] = index_count
    index_count += 1
print(field_to_index_map)

with arcpy.da.SearchCursor(fc, '*') as cursor:
    for row in cursor:
        objid = row[0]
        address_points_hash[objid] = row

for key in address_points_hash:
    print(address_points_hash[key])
    sys.exit()