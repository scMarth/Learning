import arcpy, os, httplib, json, socket, sys, urllib, requests

username = 'admin'
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

serviceUrl = "https://localhost:6443/arcgis/admin/services/FOLDER/SERVICE_NAME.MapServer"

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

params = urllib.urlencode({
    'f': 'json',
    'token': token
})

# SSL error
# response = requests.post(serviceUrl, params, headers=headers)
# print(response.text)

# this works
httpConn = httplib.HTTPConnection(serverName, serverPort)
httpConn.request("POST", serviceUrl, params, headers)
response = httpConn.getresponse()
print(response.read())



'''

  File "C:\Users\vincent-test-user\Documents\gp\SOE\print_service_minimal.py", line 51, in <module>
    response = requests.post(serviceUrl, params, headers=headers)
  File "C:\Python27\ArcGIS10.7\lib\site-packages\requests\api.py", line 110, in post
    return request('post', url, data=data, json=json, **kwargs)
  File "C:\Python27\ArcGIS10.7\lib\site-packages\requests\api.py", line 56, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Python27\ArcGIS10.7\lib\site-packages\requests\sessions.py", line 475, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Python27\ArcGIS10.7\lib\site-packages\requests\sessions.py", line 596, in send
    r = adapter.send(request, **kwargs)
  File "C:\Python27\ArcGIS10.7\lib\site-packages\requests\adapters.py", line 497, in send
    raise SSLError(e, request=request)
requests.exceptions.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:727)

'''