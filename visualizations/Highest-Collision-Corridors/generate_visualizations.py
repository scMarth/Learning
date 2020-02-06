import os, json, sys
import pandas as pd

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

        # create the path if it doesn't exist
        if not os.path.exists(output_json_dir):
            os.makedirs(output_json_dir)
        
        for i in range(len(cache)):
            curr_ind = i + 1

            out_filename = output_json_dir + '/' + str(curr_ind) + '.json'
            with open(out_filename, 'w') as out_file:
                json.dump(cache[i], out_file)

    elif sheet_name_map[sheet_ind] in ['BikeCorridors', 'Pedestrian', 'SchoolZones', 'AlcoholInvolved', 'UnsafeSpeedCorridors']:
        # get_cache_and_fields_from_type_2_df(sheet_df)
        fields, cache = get_cache_and_fields_from_type_2_df(sheet_df)

        # output json directory paths
        output_json_dir = workspace + '/json/' + sheet_name_map[sheet_ind]
        pcf_dir = output_json_dir + '/pcf'
        ct_dir = output_json_dir + '/ct'

        # create the paths if they don't exist
        for path in [output_json_dir, pcf_dir, ct_dir]:
            if not os.path.exists(path):
                os.makedirs(path)

        # write the pcf data
        

        

    



