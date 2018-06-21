# Bureau of Labor Statistics Public API Example Usage

import requests
import json
import sys

'''

SeriesID: https://www.bls.gov/help/hlpforma.htm

LA = Local Area Unemployment Statistics
U = Seasonal Adjustment Code (unadjusted)
ST0600000000000	= California
03 = unemployment rate
04 = unemployment
05 = employment
06 = labor force

'''

headers = {'Content-type': 'application/json'}
data = json.dumps({ \
    "seriesid": ['LAUST060000000000003', 'LAUST060000000000004', 'LAUST060000000000005', 'LAUST060000000000006'], \
    "startyear":"2000", \
    "endyear":"2017" \
    # "registrationkey":"" \
})
p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)

print(p.text)
print("")
# print(json_data["Results"]["series"][0]["data"][0])

records = json_data["Results"]["series"]

for i in range(0, len(records)):
    series = records[i]["data"]
    for j in reversed(range(0, len(series))):
        record = series[j]
        for key in record:
            print("series " + str(i) + " : " + "record " + str(j) + " : " + str(record[key]))

        print("")

sys.exit()

for i in reversed(range(0, len(records))):
    record = records[i]
    print("{0:4s} {1:3s} {2:11s} {3}".format( \
        record["year"], \
        record["period"], \
        record["periodName"], \
        record["value"] \
        # record["footnotes"]
    ))
    
