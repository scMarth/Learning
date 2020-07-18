# https://cityofsalinas.opendatasoft.com/pages/developers/

import requests, json

# use the search API to request data from the 'collisions' dataset
dataParams = {
    'dataset':'collisions',     # specify dataset identifier
    'format':'json',            # specify json format
    'q' : 'objectid = 1503'     # do a full text query for objectid = 1503
}

# send the post request
p = requests.post('https://cityofsalinas.opendatasoft.com/api/records/1.0/download/', data=dataParams)
json_data = json.loads(p.text) # read the response as JSON

# print the data in the resulting record
for key in json_data[0]['fields']:
    print('{} : {}'.format(key, json_data[0]['fields'][key]))