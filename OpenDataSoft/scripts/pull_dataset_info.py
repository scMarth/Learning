'''

Download ods-datasets-monitoring.json from:

https://cityofsalinas.opendatasoft.com/explore/dataset/ods-datasets-monitoring/export/?disjunctive.visibility=true&refine.visibility=&source=monitoring&refine.domain_id=cityofsalinas&dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6Im9kcy1kYXRhc2V0cy1tb25pdG9yaW5nIiwib3B0aW9ucyI6eyJkaXNqdW5jdGl2ZS52aXNpYmlsaXR5IjoidHJ1ZSIsInJlZmluZS52aXNpYmlsaXR5IjoiIiwic291cmNlIjoibW9uaXRvcmluZyIsInJlZmluZS5kb21haW5faWQiOiJjaXR5b2ZzYWxpbmFzIn19LCJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiTUFYIiwieUF4aXMiOiJwb3B1bGFyaXR5X3Njb3JlIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiIzAwM0M2MyJ9XSwieEF4aXMiOiJkYXRhc2V0X2lkIiwibWF4cG9pbnRzIjoiIiwidGltZXNjYWxlIjoiIiwic29ydCI6InNlcmllMS0xIn1dLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJ0aW1lc2NhbGUiOiIiLCJhbGlnbk1vbnRoIjp0cnVlfQ%3D%3D


'''

import json, os
import pandas as pd

workspace = os.path.dirname(__file__)
json_file = workspace + '/ods-datasets-monitoring.json'

# with open(json_file) as json_file:
#     data = json.load(json_file)
#     for dataset_info in data:
#         fields = dataset_info['fields']

#         dataset_id = fields['dataset_id']
#         title = fields['title']
#         api_call_count = fields['api_call_count']
#         popularity_score = fields['popularity_score']

#         print('dataset_id = ' + str(dataset_id))
#         print('title = ' + str(title))
#         print('api_call_count = ' + str(api_call_count))
#         print('popularity_score = ' + str(popularity_score))
#         print('')

excel_file = workspace + '/Salinas_Data_Inventory2019.xlsx'

xl = pd.ExcelFile(excel_file)
sheet1_df = xl.parse(0)

print(sheet1_df.columns)

for row in sheet1_df.iterrows():
    print(row)
    print('')