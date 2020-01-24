'''

Download the json for ods-datasets-monitoring into script-directory into a file called 'ods-datasets-monitoring.json'
Create a table mapping dataset ids to popularity score for that dataset.
Use this information to update the popularity scores in script-directory/Salinas_Data_Inventory2019.xlsx.
The result is stored in a copy of the excel file: script-directory/result.xlsx

'''
import json, os, requests, shutil, openpyxl
import pandas as pd

workspace = os.path.dirname(__file__)
json_file = workspace + '/ods-datasets-monitoring.json'

# Download the json data for 'ods-datasets-monintoring' dataset and store it in 'json_file'
dl_url = r'https://cityofsalinas.opendatasoft.com/explore/dataset/ods-datasets-monitoring/download/?format=json&timezone=America/Los_Angeles&source=monitoring'
r = requests.get(dl_url)
with open(json_file, 'wb') as f:
    f.write(r.content)

# A table mapping dataset_id's to popularity scores
dataset_popularity_scores = {}

# construct dataset_popularity_scores
with open(json_file) as json_file:
    data = json.load(json_file)
    for dataset_info in data:
        fields = dataset_info['fields']

        dataset_id = fields['dataset_id']
        popularity_score = fields['popularity_score']

        dataset_popularity_scores[dataset_id] = popularity_score

excel_file = workspace + '/Salinas_Data_Inventory2019.xlsx'
result_file = workspace + '/result.xlsx'

# copy the excel file
shutil.copyfile(excel_file, result_file)

book = openpyxl.load_workbook(result_file)
writer = pd.ExcelWriter(result_file, engine='openpyxl', date_format='m/d/yyyy', datetime_format='m/d/yyyy')
# writer = pd.ExcelWriter(result_file, engine='openpyxl')
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

# load the excel file (the first sheet)
xl = pd.ExcelFile(result_file)
sheet1_df = xl.parse(0)
# sheet1_df = xl.parse(0, dtype={'Start Date':object, 'End Date':object})
sheet1_name = xl.sheet_names[0]

# For some reason, pandas converts booleans to float, so cast it back into boolean
sheet1_df['Is Published?'] = sheet1_df['Is Published?'].astype(bool)
# Convert dates back to string
# sheet1_df['Start Date'] = sheet1_df['Start Date'].astype(str, errors='ignore')
# sheet1_df['End Date'] = sheet1_df['End Date'].astype(str, errors='ignore')

# sheet1_df['Start Date'].apply(lambda x: x.strftime('%m/%d/%Y'))

for index, row in sheet1_df.iterrows():
    column_name = sheet1_df.columns[1] # dataset_id column name

    dataset_id = row[1] # dataset id is in the second column
    popularity_score = None
    if dataset_id in dataset_popularity_scores:
        popularity_score = dataset_popularity_scores[dataset_id]
        sheet1_df.at[index, 'Open Data Score'] = popularity_score
    print('{} {} {}'.format(index + 2, row[1], popularity_score))
    print('')

print(sheet1_df['Start Date'])
print(sheet1_df.dtypes)

# print(sheet1_df.columns)

# update without overwrites
sheet1_df.to_excel(writer, sheet_name=sheet1_name, index=False)
writer.save()