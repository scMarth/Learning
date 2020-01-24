import os, json
import pandas as pd

workspace = os.path.dirname(__file__)

excel_file = workspace + '/test.xlsx'

# load the excel file
xl = pd.ExcelFile(excel_file)

# print sheet names
# print('SHEET NAMES:')
# print(xl.sheet_names)
# print('')

# get the data frame for the second sheet
sheet1_df = xl.parse(1)

# print column names
# print('COLUMN NAMES:')
# for column_name in sheet1_df.columns:
#     print(column_name)
# print('')

# build the cache for primary collision factors data
pcf_cache = []
pcf_fields = {}

for index, row in sheet1_df.iterrows():

    # the first row should have field information
    if index == 0:
        for i in range(len(row) - 1): # skip the last item (totals)
            if i != 1: # skip the second column because it's blank
                pcf_fields[i] = row[i]
    elif index >= 1 and index <= 10:
        insert = {}
        for i in range(len(row) - 1): # skip the last item (totals)
            if i != 1: # skip the second column because it's blank
                insert[pcf_fields[i]] = None if row.isna()[i] else row[i]
        pcf_cache.append(insert)

print('')
print('PCF FIELDS:')
print(pcf_fields)

print('')
print('PCF DATA:')
for item in pcf_cache:
    print(item)

# get the data frame for the third sheet
sheet2_df = xl.parse(2)

# build the cache for collision type data
ct_cache = []
ct_fields = {}

for index, row in sheet2_df.iterrows():

    # the first row should have field information
    if index == 0:
        for i in range(len(row) - 1): # skip the last item (totals)
            if i != 1: # skip the second column because it's blank
                ct_fields[i] = row[i]
    elif index >= 1 and index <= 10:
        insert = {}
        for i in range(len(row) - 1): # skip the last item (totals)
            if i != 1: # skip the second column because it's blank
                insert[ct_fields[i]] = None if row.isna()[i] else row[i]
        ct_cache.append(insert)

print('')
print('CT FIELDS:')
print(ct_fields)

print('')
print('CT DATA:')
for item in ct_cache:
    print(item)

output_json_dir = workspace + '/json'
pcf_dir = output_json_dir + '/pcf'
ct_dir = output_json_dir + '/ct'

for path in [output_json_dir, pcf_dir, ct_dir]:
    if not os.path.exists(path):
        os.makedirs(path)

for i in range(len(pcf_cache)):
    curr_ind = i + 1

    pcf_out_filename = pcf_dir + '/' + str(curr_ind) + '.json'
    with open(pcf_out_filename, 'w') as pcf_out_file:
        json.dump(pcf_cache[i], pcf_out_file)

    ct_out_filename = ct_dir + '/' + str(curr_ind) + '.json'
    with open(ct_out_filename, 'w') as ct_out_file:
        json.dump(ct_cache[i], ct_out_file)

