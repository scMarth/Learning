# Bureau of Labor Statistics Public API Example Usage

import requests
import json
import sys
import re

def removeQuotes(inputStr):
    return re.sub("\"","",inputStr)

def jsonToStr(json):
    return json.dumps(json)

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
cali_data = json.loads(p.text)["Results"]["series"][0]["data"]

# print(json.dumps(json_data["Results"]["series"][0]["data"]))

data = json.dumps({ \
    "seriesid": ['SMU06415000000000001'], \
    "startyear":"2000", \
    "endyear":"2017" \
    # "registrationkey":"" \
})

p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
salinas_data = json.loads(p.text)["Results"]["series"][0]["data"]

with open('BLS_California-Salinas_2000-2017.csv', 'w') as file:

    # write csv header
    file.write("periodName,period,salinasValue,statewideValue,year\n")
        
    for i in reversed(range(0, len(cali_data))):
        cali_record = cali_data[i]
        salinas_record = salinas_data[i]

        file.write(cali_record["periodName"] + ",") # periodName
        file.write(cali_record["period"] + ",") # period
        file.write(salinas_record["value"] + ",") # salinasValue
        file.write(cali_record["value"] + ",") # statewideValue
        file.write(cali_record["year"]) # year
        file.write("\n")
        

        

        

        
