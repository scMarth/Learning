'''

Downloads 'download-ods-datasets-monitoring.json', which contains dataset names, then reads the json.
NOTE: It doesn't have the private datasets, because no apikey or authentication is specified.

'''

import requests, os, json

dl_url = r'https://cityofsalinas.opendatasoft.com/explore/dataset/ods-datasets-monitoring/download/?format=json&timezone=America/Los_Angeles&source=monitoring'

workspace = os.path.dirname(__file__)
json_file = workspace + '/download-ods-datasets-monitoring.json'

r = requests.get(dl_url)

with open(json_file, 'wb') as f:
    f.write(r.content)

json_data = json.loads(r.content)

for key in json_data:
    print(key)
    print('')

print(len(json_data))

