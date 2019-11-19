'''
Queries CoS 311 QAlerts Data. The resulting json is dumped into workspace + 311-data.json
'''

import requests, json, os, shutil

workspace = r'\\vgisdev\apps\visualizations\QAlerts-scrapwork\json'

# POST request
dataParams = {
    'dataset':'311-alerts-qscend',
    'format':'json'
}
p = requests.post('https://cityofsalinas.opendatasoft.com/api/records/1.0/download/', data=dataParams)

json_data = json.loads(p.text)

if not os.path.exists(workspace):
    os.makedirs(workspace)

json_file_path = workspace + r'\311-data.json'

with open(json_file_path, 'w') as file:
    file.write(p.text)