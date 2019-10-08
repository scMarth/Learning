'''

Downloads 'download-ods-datasets-monitoring.js', which contains dataset names.

'''

import requests, os

dl_url = r'https://cityofsalinas.opendatasoft.com/explore/dataset/ods-datasets-monitoring/download/?format=json&timezone=America/Los_Angeles&source=monitoring'

workspace = os.path.dirname(__file__)
json_file = workspace + '/download-ods-datasets-monitoring.js'

r = requests.get(dl_url)

with open(json_file, 'wb') as f:
    f.write('var ods_monitoring = ' + r.content)