import requests, json

# use the download API to download data from the 'collisions' dataset
dataParams = {
    'dataset':'collisions',             # specify dataset identifier
    'format':'json'                     # specify json format
}
# send the post request
p = requests.post('https://cityofsalinas.opendatasoft.com/api/records/1.0/download/', data=dataParams)
json_data = json.loads(p.text) # read the response as JSON

print('{} records downloaded'.format(len(json_data)))