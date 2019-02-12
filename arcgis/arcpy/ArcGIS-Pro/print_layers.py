import arcpy

p = arcpy.mp.ArcGISProject("CURRENT")
p.importDocument(r"C:\data\data.mxd")
for m in p.listMaps():
    print(m.name)

mxd = p.listMaps("Layers")[0]
for l in mxd.listLayers():
    if l.supports("dataSource"):
        print("{}, {}".format(l.name, l.dataSource))