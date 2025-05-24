import json, urllib, http.client, os, socket, ssl

# A function that will post HTTP POST request to the server
def postToServer(serverName, serverPort, url, params):

    # Create a custom SSL context without certificate verification
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.verify_mode = ssl.CERT_NONE
    httpConn = http.client.HTTPSConnection(serverName, serverPort, context=ssl_context)

    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"
    }
    url = urllib.parse.quote(url.encode('utf-8'))
    httpConn.request("POST", url, params, headers)
    response = httpConn.getresponse()
    data = response.read()
    httpConn.close()
    return (response, data)

def getToken(username, password, serverName, serverPort):

    tokenURL = "/arcgis/admin/generateToken"
    params = urllib.parse.urlencode({
        'username': username,
        'password': password,
        'client': 'requestip',
        'f': 'json'
    })

    response, data = postToServer(serverName, serverPort, tokenURL, params)
    if (response.status != 200 or not assertJsonSuccess(data)):
        print("Error while fetching tokens from admin URL. Please check if the server is running and ensure that the username/password provided are correct")
        print(str(data))
        return
    else:
        # Extract the token from it
        token = json.loads(data)
        return token['token']


# A function that checks that the JSON response received from the server does not contain an error
def assertJsonSuccess(data):
    obj = json.loads(data)
    if 'status' in obj and obj['status'] == "error":
        return False
    else:
        return True




def startStopService(serverName, serverPort, token, folder, svcName, svcType, startOrStop):
    params = urllib.parse.urlencode({
        'token': token,
        'f': 'json'
    })
    stopOrStartUrl = "/arcgis/admin/services/" + folder + "/" + svcName + "." + svcType + "/" + startOrStop
    response, data = postToServer(serverName, serverPort, stopOrStartUrl, params)
    if (response.status != 200 or not assertJsonSuccess(data)):
        print("Error calling:{0}".format(stopOrStartURL))
        print(str(data))
    else:
        print("{}/{}.{} {} successfully.".format(
            folder,
            svcName,
            svcType,
            "started" if startOrStop == "start" else "stopped"
        ))

    
def getServiceDataFromFolder(serverName, serverPort, token, folder):
    params = urllib.parse.urlencode({
        'token': token,
        'f': 'json'
    })
    ags_admin_url = "/arcgis/admin/services/" + folder
    response, data = postToServer(serverName, serverPort, ags_admin_url, params)
    if (response.status != 200 or not assertJsonSuccess(data)):
        print("Error calling:{0}".format(ags_admin_url))
        print(str(data))
    else:
        result = json.loads(data)
        return result['services']
