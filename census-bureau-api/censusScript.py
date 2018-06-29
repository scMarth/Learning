import requests

# Census Bureau API Example Usage

import requests
import json

headers = {'Content-type': 'application/json'}
data = json.dumps({ \
})
# p = requests.post('https://api.census.gov/data/2016/pep/population', data=data, headers=headers)
p = requests.get('https://api.census.gov/data/2016/pep/population')

print(p.text)
