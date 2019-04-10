import arcpy, numpy

fc = r"\path\file.shp"

npa = arcpy.da.TableToNumPyArray(fc, '*')
for record in npa:
    print(record)