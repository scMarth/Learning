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

for index, row in sheet1_df.iterrows():
    print("ROW:")
    print(row)
    print("INDEX:")
    print(index)
    print('')