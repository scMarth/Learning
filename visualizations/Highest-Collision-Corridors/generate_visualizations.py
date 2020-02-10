import os, json, sys
import pandas as pd

color_definitions = {
    "HCC-PCF" : [
        { "color" : "#4472c4", "field_name" : "Auto R/W Violation" },
        { "color" : "#ed7d31", "field_name" : "Driving Under Influence" },
        { "color" : "#806000", "field_name" : "Following Too Closely" },
        { "color" : "#548235", "field_name" : "Improper Passing" },
        { "color" : "#a5a5a5", "field_name" : "Improper Turning" },
        { "color" : "#ffc000", "field_name" : "Other" },
        { "color" : "#c65911", "field_name" : "Other Hazardous Movement" },
        { "color" : "#00b050", "field_name" : "Other Than Driver or Ped" },
        { "color" : "#5b9bd5", "field_name" : "Ped R/W Violation" },
        { "color" : "#70ad47", "field_name" : "Pedestrian Violation" },
        { "color" : "#595959", "field_name" : "Traffic Signals and Signs" },
        { "color" : "#e7e6e6", "field_name" : "Unsafe Speed" },
        { "color" : "#002060", "field_name" : "Wrong Side of Road" }
    ],
    "HCC-Collision Type" : [
        { "color" : "#4472c4", "field_name" : "Broadside" },
        { "color" : "#ed7d31", "field_name" : "Head-On" },
        { "color" : "#a5a5a5", "field_name" : "Hit Object" },
        { "color" : "#ffc000", "field_name" : "Not Stated" },
        { "color" : "#5b9bd5", "field_name" : "Other" },
        { "color" : "#70ad47", "field_name" : "Overturned" },
        { "color" : "#002060", "field_name" : "Rear-End" },
        { "color" : "#9e480e", "field_name" : "Vehicle - Pedestrian" }
    ],
    "HCI-PCF" : [
        { "color" : "#4472c4", "field_name" : "Auto R/W Violation" },
        { "color" : "#ed7d31", "field_name" : "Driving Under Influence" },
        { "color" : "#a5a5a5", "field_name" : "Following Too Closely" },
        { "color" : "#ffc000", "field_name" : "Other" },
        { "color" : "#5b9bd5", "field_name" : "Other Hazardous Movement" },
        { "color" : "#70ad47", "field_name" : "Ped R/W Violation" },
        { "color" : "#264478", "field_name" : "Pedestrian Violation" },
        { "color" : "#9e480e", "field_name" : "Traffic Signals and Signs" },
        { "color" : "#636363", "field_name" : "Unsafe Speed" }
    ],
    "HCI-Collision Type" : [
        { "color" : "#4472c4", "field_name" : "Broadside" },
        { "color" : "#ed7d31", "field_name" : "Head-On" },
        { "color" : "#a5a5a5", "field_name" : "Hit Object" },
        { "color" : "#ffc000", "field_name" : "Not Stated" },
        { "color" : "#5b9bd5", "field_name" : "Other" },
        { "color" : "#70ad47", "field_name" : "Rear-End" },
        { "color" : "#264478", "field_name" : "Vehicle - Pedestrian" }
    ],
    "BikeCorridors" : {
        "PCF" : [
            { "color" : "#4472c4", "field_name" : "Auto R/W Violation" },
            { "color" : "#ed7d31", "field_name" : "Driving Under Influence" },
            { "color" : "#a5a5a5", "field_name" : "Pedestrian Violation" },
            { "color" : "#ffc000", "field_name" : "Traffic Signals and Signs" },
            { "color" : "#5b9bd5", "field_name" : "Wrong Side of Road" }
        ],
        "CT": [
            { "color" : "#4472c4", "field_name" : "Broadside" },
            { "color" : "#ed7d31", "field_name" : "Other" },
            { "color" : "#a5a5a5", "field_name" : "Vehicle - Pedestrian" }
        ]
    },
    "Pedestrian" : {
        "PCF" : [
            { "color" : "#4472c4", "field_name" : "Other"},
            { "color" : "#ed7d31", "field_name" : "Ped R/W Violation"},
            { "color" : "#a5a5a5", "field_name" : "Pedestrian Violation"},
            { "color" : "#ffc000", "field_name" : "Traffic Signals and Signs"}
        ],
        "CT": [
            { "color" : "#4472c4", "field_name" : "Vehicle - Pedestrian" }
        ]
    },
    "SchoolZones" : {
        "PCF" : [
            { "color" : "#4472c4", "field_name" : "Driving Under Influence" },
            { "color" : "#ed7d31", "field_name" : "Improper Turning" },
            { "color" : "#a5a5a5", "field_name" : "Other" },
            { "color" : "#ffc000", "field_name" : "Ped R/W Violation" },
            { "color" : "#5b9bd5", "field_name" : "Pedestrian Violation" },
            { "color" : "#70ad47", "field_name" : "Traffic Signals and Signs" },
            { "color" : "#264478", "field_name" : "Unknown" }

        ],
        "CT": [
            { "color" : "#4472c4", "field_name" : "Broadside" },
            { "color" : "#ed7d31", "field_name" : "Head-On" },
            { "color" : "#a5a5a5", "field_name" : "Hit Object" },
            { "color" : "#ffc000", "field_name" : "Rear-End" },
            { "color" : "#5b9bd5", "field_name" : "Vehicle - Pedestrian" }
        ]
    },
    "AlcoholInvolved" : {
        "PCF" : [
            { "color" : "#4472c4", "field_name" : "Auto R/W Violation" },
            { "color" : "#ed7d31", "field_name" : "Driving Under Influence" },
            { "color" : "#a5a5a5", "field_name" : "Improper Turning" },
            { "color" : "#ffc000", "field_name" : "Other" },
            { "color" : "#5b9bd5", "field_name" : "Pedestrian Violation" }
        ],
        "CT": [
            { "color" : "#4472c4", "field_name" : "Broadside" },
            { "color" : "#ed7d31", "field_name" : "Head-On" },
            { "color" : "#a5a5a5", "field_name" : "Hit Object" },
            { "color" : "#ffc000", "field_name" : "Not Stated" },
            { "color" : "#5b9bd5", "field_name" : "Rear-End" },
            { "color" : "#70ad47", "field_name" : "Vehicle - Pedestrian" }
        ]
    },
    "UnsafeSpeedCorridors" : {
        "PCF" : [
            { "color" : "#4472c4", "field_name" : "Unsafe Speed" }
        ],
        "CT": [
            { "color" : "#4472c4", "field_name" : "Broadside" },
            { "color" : "#ed7d31", "field_name" : "Hit Object" },
            { "color" : "#a5a5a5", "field_name" : "Not Stated" },
            { "color" : "#ffc000", "field_name" : "Rear-End" }
        ]
    }
}

def get_cache_and_fields_from_type_1_df(df):
    # get the fields
    fields = {}
    for i in range(len(df.columns)):
        field = df.columns[i]
        if i != 1 and i < (len(df.columns) - 1): # skip the second column because it's empty, skip last column
            fields[i] = field
    
    # get the data
    cache = []
    for index, row in df.iterrows():
        if index < 10: # we're only concerned with the top 10 data
            insert = {}
            for i in range(len(row)):
                if i in fields: # grab value for fields we're interested in
                    insert[fields[i]] = None if row.isna()[i] else row[i]
            cache.append(insert)

    return [fields, cache]

def get_cache_and_fields_from_type_2_df(df):
    fields = {
        'PCF' : {},
        'CT' : {}
    }

    # get pcf fields
    for i in range(len(df.iloc[0])):
        val = df.iloc[0][i]
        if i != 1: # skip the second column because it's empty, skip the last column
            if val == 'Totals':
                break
            fields['PCF'][i] = val

    # get cf fields
    for i in range(len(df.iloc[25])):
        val = df.iloc[25][i]
        if i != 1: # skip the second column because it's empty, skip the last column
            if val == 'Totals':
                break
            fields['CT'][i] = val

    cache = {
        'PCF' : [],
        'CT' : []
    }

    # get pcf data
    for row_ind in [1, 2, 3]:
        row = df.iloc[row_ind]
        insert = {}
        for i in fields['PCF']:
            insert[fields['PCF'][i]] = None if row.isna()[i] else row[i]
        cache['PCF'].append(insert)

    for row_ind in [26, 27, 28]:
        row = df.iloc[row_ind]
        insert = {}
        for i in fields['CT']:
            insert[fields['CT'][i]] = None if row.isna()[i] else row[i]
        cache['CT'].append(insert)

    return [fields, cache]

# generates an html file
def generate_html_file(html_path, title, json_path, colors):
    with open(html_path, 'w') as file:
        file.write('<!DOCTYPE html>' + '\n')
        file.write('<html lang="en">' + '\n')
        file.write('<head>' + '\n')
        file.write('    <meta charset="UTF-8">' + '\n')
        file.write('    <title>' + title + '</title' + '\n')
        file.write('    <script src="../../lib/Chart.bundle.min.js"></script>' + '\n')
        file.write('    <script src="../../lib/Chart.min.js"></script>' + '\n')
        file.write('    <script src="../../lib/jquery-3.4.1.min.js"></script>' + '\n')
        file.write('    <script src="../../js/utils.js"></script>' + '\n')
        file.write('    <link rel="stylesheet" href="../../css/styles.css">\n')
        file.write('</head>' + '\n')
        file.write('<body>' + '\n')
        file.write('    <div id="canvas-holder">' + '\n')
        file.write('        <canvas id="chart-area"></canvas>' + '\n')
        file.write('    </div>' + '\n\n')
        file.write('    <script>' + '\n')
        file.write('        $.getJSON("' + json_path + '", data => {\n')
        file.write('            createChartFromJSON(data, [' + '\n')
        file.write('                ' + ',\n                '.join(['"' + x + '"' for x in colors]) + '\n')
        file.write('            ]);\n')
        file.write('        });\n')
        file.write('    </script>\n')
        file.write('</body>\n')
        file.write('</html>\n')

workspace = os.path.dirname(__file__)

excel_file = workspace + '/test.xlsx'

# load the excel file
xl = pd.ExcelFile(excel_file)

# print sheet names
print('SHEET NAMES:')
print(xl.sheet_names)
print('')

# mapping from sheet index to sheet name
sheet_name_map = {}
for i in range(len(xl.sheet_names)):
    name = xl.sheet_names[i]
    sheet_name_map[i] = name

for sheet_ind in sheet_name_map:
    # skip the first sheet
    if sheet_ind == 0:
        continue

    sheet_df = xl.parse(sheet_ind)

    fields = None
    cache = None

    if sheet_name_map[sheet_ind] in ['HCC-PCF', 'HCC-Collision Type', 'HCI-PCF', 'HCI-Collision Type']:
        fields, cache = get_cache_and_fields_from_type_1_df(sheet_df)

        # output json directory path
        output_json_dir = workspace + '/json/' + sheet_name_map[sheet_ind]
        output_html_dir = workspace + '/html/' + sheet_name_map[sheet_ind]

        # create the path if it doesn't exist
        for path in [output_json_dir, output_html_dir]:
            if not os.path.exists(path):
                os.makedirs(path)

        for i in range(len(cache)):
            curr_ind = i + 1

            out_filename = output_json_dir + '/' + str(curr_ind) + '.json'
            with open(out_filename, 'w') as out_file:
                json.dump(cache[i], out_file)

            out_html_file_path = output_html_dir + '/' + str(curr_ind) + '.html'
            html_file_json_path = '../../json/' + sheet_name_map[sheet_ind] + '/' + str(curr_ind) + '.json'
            title = sheet_name_map[sheet_ind] + ' - Chart ' + str(curr_ind)
            colors = [x['color'] for x in color_definitions[sheet_name_map[sheet_ind]]]
            generate_html_file(out_html_file_path, title, html_file_json_path, colors)

    elif sheet_name_map[sheet_ind] in ['BikeCorridors', 'Pedestrian', 'SchoolZones', 'AlcoholInvolved', 'UnsafeSpeedCorridors']:
        # get_cache_and_fields_from_type_2_df(sheet_df)
        fields, cache = get_cache_and_fields_from_type_2_df(sheet_df)

        # output json directory paths
        output_json_dir = workspace + '/json/' + sheet_name_map[sheet_ind]
        output_html_dir = workspace + '/html/' + sheet_name_map[sheet_ind]
        pcf_dir = output_json_dir + '/PCF'
        ct_dir = output_json_dir + '/CT'
        html_pcf_dir = output_html_dir + '/PCF'
        html_ct_dir = output_html_dir + '/CT'


        # create the paths if they don't exist
        for path in [output_json_dir, output_html_dir, pcf_dir, ct_dir, html_pcf_dir, html_ct_dir]:
            if not os.path.exists(path):
                os.makedirs(path)

        # write the pcf data
        for i in range(len(cache['PCF'])):
            curr_ind = i + 1
            pcf_out_filename = pcf_dir + '/' + str(curr_ind) + '.json'
            with open(pcf_out_filename, 'w') as pcf_out_file:
                json.dump(cache['PCF'][i], pcf_out_file)

            out_html_file_path = output_html_dir + '/PCF/' + str(curr_ind) + '.html'
            html_file_json_path = '../../json/' + sheet_name_map[sheet_ind] + '/PCF/' + str(curr_ind) + '.json'
            title = sheet_name_map[sheet_ind] + ' - PCF Chart ' + str(curr_ind)
            colors = [x['color'] for x in color_definitions[sheet_name_map[sheet_ind]]['PCF']]
            generate_html_file(out_html_file_path, title, html_file_json_path, colors)

        for i in range(len(cache['CT'])):
            curr_ind = i + 1
            ct_out_filename = ct_dir + '/' + str(curr_ind) + '.json'
            with open(ct_out_filename, 'w') as ct_out_file:
                json.dump(cache['CT'][i], ct_out_file)

            out_html_file_path = output_html_dir + '/CT/' + str(curr_ind) + '.html'
            html_file_json_path = '../../json/' + sheet_name_map[sheet_ind] + '/CT/' + str(curr_ind) + '.json'
            title = sheet_name_map[sheet_ind] + ' - CT Chart ' + str(curr_ind)
            colors = [x['color'] for x in color_definitions[sheet_name_map[sheet_ind]]['CT']]
            generate_html_file(out_html_file_path, title, html_file_json_path, colors)


        

        

    



