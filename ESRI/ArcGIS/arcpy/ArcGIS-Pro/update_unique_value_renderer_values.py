import os, arcpy, string, sys
from arcpy import env

pro_projects = [
    # "D:\Templates\TransRanchTemplatePro_Hectares\TransRanchTemplatePro_Hectares.aprx",
    "D:\Templates\TransRanchTemplatePro_Hectares2\TransRanchTemplatePro_Hectares2.aprx"
]

for path in pro_projects:
    aprx = arcpy.mp.ArcGISProject(path)
    map = aprx.listMaps("Layers")[0]
    layer = map.listLayers("*RPT_APPLICATION_BLOCKS_V*")[0]

    print('path: {}'.format(path))

    # Check if layer has unique values symbology
    if layer.symbology and layer.symbology.renderer == 'UniqueValueRenderer':

        layer.symbology.renderer.fields = ["VARIETY"]

        # determine missing values
        missing_val_list = []

        missing_vals = layer.symbology.renderer.listMissingValues()

        for val in missing_vals:
            # print('missing value: {}'.format(val))
            # print('val.heading: {}'.format(val.heading))
            if val.heading == 'VARIETY':
                items = val.items
                for item in items:

                    if item.values[0][0]:
                        missing_val_list.append(item.values[0][0])
            else:
                continue
        
        print('missing values:')
        for val in missing_val_list:
            print(val)

        sym = layer.symbology

        sym.renderer.addValues({
            "VARIETY": missing_val_list
        })
        layer.symbology = sym
        aprx.save()

        print('after:')

        # determine missing values
        missing_val_list = []

        missing_vals = layer.symbology.renderer.listMissingValues()

        for val in missing_vals:
            # print('missing value: {}'.format(val))
            # print('val.heading: {}'.format(val.heading))
            if val.heading == 'VARIETY':
                items = val.items
                for item in items:

                    if item.values[0][0]:
                        missing_val_list.append(item.values[0][0])
            else:
                continue
        
        print('missing values:')
        for val in missing_val_list:
            print(val)


    
    print('')

    
