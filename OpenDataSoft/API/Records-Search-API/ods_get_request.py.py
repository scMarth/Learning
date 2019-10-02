import http.client, json

# GET REQUEST
# https://cityofsalinas.opendatasoft.com/api/records/1.0/search/?dataset=anonymized-crime-data&sort=address100&rows=100

conn = http.client.HTTPSConnection("cityofsalinas.opendatasoft.com")
conn.request("GET", "/api/records/1.0/search/?dataset=anonymized-crime-data&sort=address100&rows=100")

r1 = conn.getresponse()
print r1.status, r1.reason
# print r1.read()
json_data = json.loads(r1.read())

# print the number of records found
print(str(len(json_data['records'])) + " records found\n")

# print the addresses
print("Addresses:")
for i in range(0,len(json_data['records'])):
    print("\t" + str(json_data['records'][i]['fields']['address100']))
