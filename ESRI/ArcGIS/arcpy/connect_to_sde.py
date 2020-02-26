import arcpy, sys

# read authorotative list of address points into memory
hash_table = {}
fc = r'\\server\MyProject\test.sde\CRW_NET.dbo.fc_name'
with arcpy.da.SearchCursor(fc, '*') as cursor:
    for row in cursor:
        objid = row[0]
        hash_table[objid] = row
        print(row)
        sys.exit()