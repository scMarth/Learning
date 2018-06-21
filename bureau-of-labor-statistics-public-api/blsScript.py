# Bureau of Labor Statistics Public API Example Usage

import requests
import json

headers = {'Content-type': 'application/xml'}
data = json.dumps({ \
    "seriesid": ['CES0000000001'], \
    "startyear":"2011", \
    "endyear":"2014", \
    # "registrationkey":"" \
})
p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)

print(p.text)
