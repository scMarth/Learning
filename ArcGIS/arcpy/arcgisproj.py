# this doesn't create a new ArcGIS Pro Project file. It seems that it must already exist for this code to work.

import arcpy

path = r'.\blank.aprx'

aprx = arcpy.mp.ArcGISProject(path)

print("Done")
