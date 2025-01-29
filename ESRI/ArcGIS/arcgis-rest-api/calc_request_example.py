import os, requests, urllib, json, sys


username = os.environ['username']
password = os.environ['password']
protocol = str("https://")





# get a token
get_token_url = "https://domain.com/arcgis/tokens/generateToken"
payload = {
  'username' : username,
  'password' : password,
  'client' : 'requestip',
  'f' : 'json'
}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

payload = urllib.parse.urlencode(payload)

response = requests.request("POST", get_token_url, headers=headers, data=payload)
token = json.loads(response.text)['token']
print('token: {}'.format(token))











# update record with NUMBER = 990494
update_url = "https://domain.com/arcgis/rest/services/FOLDER/SVC/FeatureServer/0/calculate"

num = 990494

# construct payload parameter
expr = [
    {"field": "ATTRIB1", "value": 999999999999999},
    {"field": "ATTRIB2", "value": 999999999999999} # if you comment out this line, it will only update the other attribute
]

payload = {
    'calcExpression': json.dumps(expr),
    'where': 'NUMBER = {}'.format(num),
    'token': token,
    'f': 'json'
}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

payload = urllib.parse.urlencode(payload)
response = requests.request("POST", update_url, headers=headers, data=payload)
print(response.text)










# SAME AS LAST CALL, ONLY UPDATES 1 ATTRIBUTE and sets value to NULL
# update record with NUMBER = 5 and print the response
update_url = "https://domain.com/arcgis/rest/services/FOLDER/SVC/FeatureServer/0/calculate"

ranch_number = 5

expr = [
    {"field": "CUSTOMER_ACCOUNT_SITE_ID", "value": "Null"}
]

payload = {
    'calcExpression': json.dumps(expr),
    'where': 'TRANSACTIONAL_RANCH_NUMBER = {}'.format(ranch_number),
    'token': token,
    'f': 'json'
}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

payload = urllib.parse.urlencode(payload)
response = requests.request("POST", update_url, headers=headers, data=payload)
print(response.text)


