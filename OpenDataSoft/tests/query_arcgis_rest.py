import requests, json, os, shutil

workspace = os.path.dirname(__file__)

# POST request
dataParams = {
    'outFields':'*',
    'objectIds':1,
    'f':'json'
}
p = requests.post('https://giswebservices.ci.salinas.ca.us/arcgis/rest/services/PublishedServices/Zoning/MapServer/0/query', data=dataParams)

json = json.loads(p.text)
print(json['features'][0]['attributes'])

'''

{'OBJECTID': 1, 'PERIMETER': 1271.6336615, 'ZONING_': 2, 'ZONING_ID': 1, 'ZONE': 'R-M-3.6', 'ACRES': 2.2, 'AREA': 95456.625, 'Shape_Length': 1271.633661975949, 'Shape_Area': 95456.6399100165, 'GlobalID': '{15E87CC9-C687-4FE2-A4E7-0873E3AD3176}', 'created_user': None, 'created_date': None, 'last_edited_user': 'RANDYC', 'last_edited_date': 1556909071000, 'DISTRICT': 'Residential Medium Density (RM)'}

'''