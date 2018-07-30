import requests

p = requests.get('https://cityofsalinas.opendatasoft.com/api/records/1.0/search/?dataset=libraries&sort=libraryname&facet=apn&facet=libraryname')

print(p.text)
