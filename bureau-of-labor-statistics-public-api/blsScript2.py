# Bureau of Labor Statistics Public API Example Usage

import requests
import json
import sys

'''

SeriesID: https://www.bls.gov/help/hlpforma.htm

CES0000000001

CE = Employment & Unemployment
S = Seasonally Adjusted
00000000 = Total nonfarm
01 = all employees, thousands

'''

headers = {'Content-type': 'application/json'}
data = json.dumps({ \
    "seriesid": ['CES0000000001'], \
    "startyear":"2000", \
    "endyear":"2017" \
    # "registrationkey":"" \
})
p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)

print(p.text)
print("")
# print(json_data["Results"]["series"][0]["data"][0])

records = json_data["Results"]["series"][0]["data"]
print(records[0])
print("")

for i in reversed(range(0, len(records))):
    record = records[i]
    print("{0:4s} {1:3s} {2:11s} {3}".format( \
        record["year"], \
        record["period"], \
        record["periodName"], \
        record["value"] \
        # record["footnotes"]
    ))
    
