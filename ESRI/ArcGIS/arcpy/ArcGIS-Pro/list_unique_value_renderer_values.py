import os, arcpy, string, sys
from arcpy import env

pro_projects = [
    "D:\Templates\TransRanchTemplatePro_Hectares\TransRanchTemplatePro_Hectares.aprx",
    "D:\Templates\TransRanchTemplatePro_Hectares2\TransRanchTemplatePro_Hectares2.aprx"
]

basepath = os.path.dirname(os.path.abspath(__file__))
output_file = basepath + r'\list_renderer_values_output.txt'

# delete output file if it exists
if os.path.exists(output_file):
    os.remove(output_file)

def print_to_file(input_data):
    with open(output_file, 'a') as file:
        file.write('{}\n'.format(input_data))

for path in pro_projects:
    aprx = arcpy.mp.ArcGISProject(path)
    map = aprx.listMaps("Layers")[0]
    layer = map.listLayers("*RPT_APPLICATION_BLOCKS_V*")[0]

    print_to_file('path: {}'.format(path))

    # Check if layer has unique values symbology
    if layer.symbology and layer.symbology.renderer == 'UniqueValueRenderer':
        print_to_file('value field: {}'.format(layer.symbology.renderer.fields))


        
        # Set value field
        # layer.symbology.renderer.fields = ["VARIETY"]

        # find current values
        current_values = []
        groups = layer.symbology.renderer.groups
        for group in groups:
            if group.heading == 'VARIETY':
                for item in group.items:
                    current_values.append(item.values[0][0])


        # determine missing values
        missing_val_list = []

        missing_vals = layer.symbology.renderer.listMissingValues()

        # print('missing_vals: {}'.format(missing_vals))

        for val in missing_vals:
            # print('missing value: {}'.format(val))
            # print('val.heading: {}'.format(val.heading))
            if val.heading == 'VARIETY':
                items = val.items
                for item in items:
                    # print('item.description: {}'.format(item.description))
                    # print('item.label: {}'.format(item.label))
                    # print('item.symbol: {}'.format(item.symbol))
                    # print('item.values: {}'.format(item.values)
                    # )
                    # print('value: {}'.format(item.values[0][0]))
                    # print('')
                    if item.values[0][0]:
                        missing_val_list.append(item.values[0][0])
            else:
                continue
        
        print_to_file('values:')
        for val in current_values:
            print_to_file(val)
        
        print_to_file('')
        
        print_to_file('missing values:')
        for val in missing_val_list:
            print_to_file(val)
    
    print_to_file('')