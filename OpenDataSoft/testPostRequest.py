import requests
import json

# POST request
dataParams = {
    'dataset':'anonymized-crime-data',
    'sort':'address100', # date occurred on
    'rows':'100' # request 100 records
}
p = requests.post('https://cityofsalinas.opendatasoft.com/api/records/1.0/search/', data=dataParams)

json_data = json.loads(p.text)

# print the number of records found
print(str(len(json_data['records'])) + " records found\n")

# print the addresses
print("Addresses:")
for i in range(0,len(json_data['records'])):
    print("\t" + str(json_data['records'][i]['fields']['address100']))
