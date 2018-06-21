import requests
import json

headers = {'Content-type': 'application/json'}
data = json.dumps({ \
    "seriesid": ['CES0000000001'], \
    "startyear":"2011", \
    "endyear":"2014", \
    # "registrationkey":"" \
})
p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)

print(p.text)
print("")
print(json_data["Results"]["series"][0]["data"][0])

# print json.dumps(json_data, indent=4, separators=(',',': '))
