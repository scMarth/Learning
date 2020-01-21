import os
import pandas as pd

workspace = os.path.dirname(__file__)

excel_file = workspace + '/test.xlsx'

# load the excel file
xl = pd.ExcelFile(excel_file)

# print sheet names
print('SHEET NAMES:')
print(xl.sheet_names)
print('')

# get the data frame for a sheet
sheet1_df = xl.parse(1)

# print column names
print('COLUMN NAMES:')
for column_name in sheet1_df.columns:
    print(column_name)
print('')

# build the cache for primary collision factors data
pcf_cache = []
pcf_fields = {}

for index, row in sheet1_df.iterrows():
    print(row.name)
    print(row.dtype)
    print(row.isna())

    # the first row should have field information
    if index == 0:
        for i in range(len(row)):
            if i != 1: # skip the second column because it's blank
                pcf_fields[i] = row[i]
    elif index >= 1 and index <= 10:
        insert = {}
        for i in range(len(row)):
            if i != 1: # skip the second column because it's blank
                insert[pcf_fields[i]] = None if row.isna()[i] else row[i]
        pcf_cache.append(insert)

print('')
print(pcf_fields)

print('')
for item in pcf_cache:
    print(item)