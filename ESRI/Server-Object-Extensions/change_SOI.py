# this example changes the enabled SOI on a service

import arcpy, os, httplib, json, socket, urllib

username = 'sysadmin'
password = 'enter_pass_here'

# get IPV4 address
hostname = socket.gethostname()
serverName = socket.gethostbyname(hostname) # IPV4 Address

serverPort = 6080

def getToken(username, password, serverName, serverPort):
    tokenURL = "/arcgis/admin/generateToken"
    params = urllib.urlencode({'username': username, 'password': password, 'client': 'requestip', 'f': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

    # Connect to URL and post parameters
    httpConn = httplib.HTTPConnection(serverName, serverPort)
    httpConn.request("POST", tokenURL, params, headers)

    # Read response
    response = httpConn.getresponse()
    if (response.status != 200):
        httpConn.close()
        print("Error while fetching tokens from admin URL. Please check the URL and try again.")
        return
    else:
        data = response.read()
        httpConn.close()

        obj = json.loads(data)
        if 'status' in obj and obj['status'] == "error":
            return

        # Extract the token from it
        return obj['token']

token = getToken(username, password, serverName, serverPort)

serviceUrl = "/arcgis/admin/services/FOLDER/SERVICE_NAME.MapServer"
params = urllib.urlencode({'token': token, 'f': 'json'})
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
httpConn = httplib.HTTPConnection(serverName, serverPort)
httpConn.request("POST", serviceUrl, params, headers)
response = httpConn.getresponse()
data = response.read()
dataObj = json.loads(data)
print(dataObj)
httpConn.close()

# change the enabled extensions
for ext in dataObj['extensions']:
    if ext['typeName'] == "SOI_1":
        ext['enabled'] = 'FALSE'
    if ext['typeName'] == "SOI_2":
        ext['enabled'] = 'FALSE'
    if ext['typeName'] == "SOI_3":
        ext['enabled'] = 'TRUE'

# set the SOI order
dataObj['frameworkProperties']['interceptorOrderList'] = "SOI_3"

editUrl = "https://localhost:8080/arcgis/admin/services/FOLDER/SERVICE_NAME.MapServer/edit"
editServiceParams = urllib.urlencode({'token': token, 'f': 'json', 'service': json.dumps(dataObj)})
httpConn.request("POST", editUrl, editServiceParams, headers)
updateServiceResponse = httpConn.getresponse()

print('')
print(updateServiceResponse.read())
print(updateServiceResponse)
print(updateServiceResponse.msg)
print(updateServiceResponse.status)