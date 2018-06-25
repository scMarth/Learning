# Bureau of Labor Statistics Public API Example Usage

import requests
import json
import sys

'''

SeriesID: https://www.bls.gov/help/hlpforma.htm

SMU06415000000000001

SM = State and Area Employment, Hours, and Earnings
U = Not Seasonally Adjusted
06 = California

Area Codes
    41500 = Salinas-Seaside-Monterey
    00000 = Statewide

00000000 = Total Nonfarm
01 = All Employees, In Thousands

'''

headers = {'Content-type': 'application/json'}
data = json.dumps({ \
    "seriesid": ['SMU06000000000000001'], \
    "startyear":"2000", \
    "endyear":"2017" \
    # "registrationkey":"" \
})
p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)

# print(json.dumps(json_data["Results"]["series"][0]["data"]))


with open('BLS-SMU06000000000000001_California-Employees-2000-2017.json', 'w') as file:
    file.write(json.dumps(json_data["Results"]["series"][0]["data"]))

data = json.dumps({ \
    "seriesid": ['SMU06415000000000001'], \
    "startyear":"2000", \
    "endyear":"2017" \
    # "registrationkey":"" \
})

p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)

with open('BLS-SMU06000000000000001_Salinas-Employees-2000-2017.json', 'w') as file:
    file.write(json.dumps(json_data["Results"]["series"][0]["data"]))
