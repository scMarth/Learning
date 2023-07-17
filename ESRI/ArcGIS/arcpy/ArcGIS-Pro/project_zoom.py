import os, arcpy, string, sys
from arcpy import env

pro_projects = [
    # "D:\Templates\TransRanchTemplatePro_Hectares\TransRanchTemplatePro_Hectares.aprx",
    # "D:\Templates\TransRanchTemplatePro_Hectares2\TransRanchTemplatePro_Hectares2.aprx",
    "D:\Templates\TransRanchTemplatePro_Hectares5\TransRanchTemplatePro_Hectares5.aprx"
]

for path in pro_projects:
    aprx = arcpy.mp.ArcGISProject(path)
    map = aprx.listMaps("Layers")[0]
    layer = map.listLayers("*RPT_APPLICATION_BLOCKS_V*")[0]

    print('path: {}'.format(path))

    # apparently these are meant to be used when Pro is open, if you try to use these from an outside script, it will always return none according to the pro project documentation
    # print('aprx.activeMap: {}'.format(aprx.activeMap))
    # print('aprx.activeView: {}'.format(aprx.activeView))

    where = "TRANSACTIONAL_RANCH_NUMBER = {0} AND IS_ACTIVE = 'Yes'".format(16903)

    arcpy.SelectLayerByAttribute_management(layer, 'NEW_SELECTION', where)

    lyt = aprx.listLayouts()[0]

    mf = lyt.listElements('MAPFRAME_ELEMENT', '*')[0]

    mf.camera.setExtent(mf.getLayerExtent(layer,True,True))
    mf.zoomToAllLayers()

    aprx.save()

    sys.exit()


'''

import arcpy


project = arcpy.mp.ArcGISProject("//mapserver/blah/Pro-workforce2.aprx")
map = project.listMaps()[0]

whereZoom = "BlahID = '20181520528'"

layer = map.listLayers("Zoom")[0]
arcpy.SelectLayerByAttribute_management(layer,"NEW_SELECTION",whereZoom)

lyt = project.listLayouts()[0]

mf = lyt.listElements('MAPFRAME_ELEMENT','*')[0]
mf.camera.setExtent(mf.getLayerExtent(layer,True,True))
mf.zoomToAllLayers()


lyt.exportToPDF("//mapserver/blah/test-%s.pdf" % whereZoom)

'''