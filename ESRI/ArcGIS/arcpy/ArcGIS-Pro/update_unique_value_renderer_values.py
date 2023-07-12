import os, arcpy, string, sys
from arcpy import env

pro_projects = [
    # "D:\Templates\TransRanchTemplatePro_Hectares\TransRanchTemplatePro_Hectares.aprx",
    # "D:\Templates\TransRanchTemplatePro_Hectares2\TransRanchTemplatePro_Hectares2.aprx",
    "D:\Templates\TransRanchTemplatePro_Hectares3\TransRanchTemplatePro_Hectares3.aprx"
]

for path in pro_projects:
    aprx = arcpy.mp.ArcGISProject(path)
    map = aprx.listMaps("Layers")[0]
    layer = map.listLayers("*RPT_APPLICATION_BLOCKS_V*")[0]

    print('path: {}'.format(path))

    # Check if layer has unique values symbology
    if layer.symbology and layer.symbology.renderer == 'UniqueValueRenderer':

        sym = layer.symbology

        # determine missing values
        missing_val_list = []

        missing_vals = sym.renderer.listMissingValues()
        for val in missing_vals:
            if val.heading == 'VARIETY':
                items = val.items
                for item in items:
                    if item.values[0][0]:
                        missing_val_list.append(item.values[0][0])
        
        print('missing values:')
        for val in missing_val_list:
            print(val)
        print('')


        # find current values
        current_values = []
        groups = layer.symbology.renderer.groups
        for group in groups:
            if group.heading == 'VARIETY':
                for item in group.items:
                    current_values.append(item.values[0][0])
        
        print('current values:')
        for val in current_values:
            print(val)
        print('')

        # remove values
        sym.renderer.removeValues({"VARIETY" : current_values})

        current_values_after = []
        groups = sym.renderer.groups
        for group in groups:
            if group.heading == 'VARIETY':
                for item in group.items:
                    current_values_after.append(item.values[0][0])

        print('after remove values:')
        for val in current_values_after:
            print(val)
        print('')

        sym.renderer.fields = ["VARIETY"]

        all_values = current_values + missing_val_list
        all_values.sort()

        print('all values:')
        for val in all_values:
            print(val)

        sym.renderer.addValues({
            "VARIETY": missing_val_list
        })

        layer.symbology = sym
        aprx.save()


    print('')

    
