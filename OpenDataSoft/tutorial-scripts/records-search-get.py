import requests, json

# use the search API to request data from the 'libraries' dataset
p = requests.get('https://cityofsalinas.opendatasoft.com/api/records/1.0/search/?dataset=libraries')
json_data = json.loads(p.text) # read the response as JSON

for record in json_data['records']:
    print(record['fields']['libraryname']) # print the library name