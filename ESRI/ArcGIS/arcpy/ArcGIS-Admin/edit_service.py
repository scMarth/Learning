# configure map service with ags admin

import json, urllib, http.client, os, socket, ssl

import service_config

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

def editMapService(serverName, serverPort, token, folder, service_name, service_payload):
    params = urllib.parse.urlencode({
        'service': json.dumps(service_payload),
        'token': token,
        'f': 'json'
    })
    ags_admin_url = "/arcgis/admin/services/" + folder
    svc_url = "/arcgis/admin/services/{}/{}.MapServer/edit".format(folder, service_name)
    response, data = postToServer(serverName, serverPort, svc_url, params)
    if (response.status != 200 or not assertJsonSuccess(data)):
        print("Error calling:{0}".format(svc_url))
        print(str(data))
    else:
        result = json.loads(data)
        return result


def getServiceData(serverName, serverPort, token, folder, service_name):
    params = urllib.parse.urlencode({
        'token': token,
        'f': 'json'
    })
    ags_admin_url = "/arcgis/admin/services/" + folder
    svc_url = "/arcgis/admin/services/{}/{}.MapServer".format(folder, service_name)
    response, data = postToServer(serverName, serverPort, svc_url, params)
    if (response.status != 200 or not assertJsonSuccess(data)):
        print("Error calling:{0}".format(svc_url))
        print(str(data))
    else:
        result = json.loads(data)
        return result

def setServiceProvider(serverName, serverPort, token, folder, service_name, provider):
    params = urllib.parse.urlencode({
        'provider': provider,
        'token': token,
        'f': 'json'
    })
    ags_admin_url = "/arcgis/admin/services/" + folder
    svc_url = "/arcgis/admin/services/{}/{}.MapServer/changeProvider".format(folder, service_name)
    response, data = postToServer(serverName, serverPort, svc_url, params)
    if (response.status != 200 or not assertJsonSuccess(data)):
        print("Error calling:{0}".format(svc_url))
        print(str(data))
    else:
        result = json.loads(data)
        return result


username = 'admin'
password = os.environ["ATLAS_AGS_ADMIN_PASSWORD"]
hostname = socket.gethostname()
serverName = socket.gethostbyname(hostname) # IPV4 Address
serverPort = 6443

token = getToken(username, password, serverName, serverPort)

for env in service_config.configs:
    env_name = env['env_name']

    if env_name != 'TEST':
        continue

    configs = env['configs']

    for folder in configs:
        folder_name = folder['folder_name']
        folder_services = folder['services']

        if folder_name != "ATLAS":
            continue

        print('folder: {}'.format(folder_name))

        for service in folder_services:

            service_name = service + "_2"

            if service_name != 'GEOGRAPHIES_2':
                continue

            svc_settings = folder_services[service]

            print(svc_settings)

            # get object representing the service data
            svc_data = getServiceData(serverName, serverPort, token, folder_name, service_name)

            # set min instances per node
            if 'minInstancesPerNode' in svc_data and 'minInstancesPerNode' in svc_settings:
                svc_data['minInstancesPerNode'] = svc_settings['minInstancesPerNode']

            # set max instances per node
            if 'maxInstancesPerNode' in svc_data and 'maxInstancesPerNode' in svc_settings:
                svc_data['maxInstancesPerNode'] = svc_settings['maxInstancesPerNode']

            # set max wait time for service
            if 'maxWaitTime' in svc_data and 'maxWaitTime' in svc_settings:
                svc_data['maxWaitTime'] = svc_settings['maxWaitTime']
            
            if 'FeatureServerEnabled' in svc_settings:
                if svc_settings['FeatureServerEnabled'] and 'FeatureServerCapabilities' in svc_settings:
                    if 'extensions' in svc_data:
                        for extension in svc_data['extensions']:
                            if extension['typeName'] == 'FeatureServer':
                                extension['enabled'] = svc_settings['FeatureServerEnabled']
                                extension['capabilities'] = svc_settings['FeatureServerCapabilities']

            print('svc_data: {}'.format(svc_data))

            print('updating service...')
            response = editMapService(serverName, serverPort, token, folder_name, service_name, svc_data)
            print(response)

            # set the provider (shared vs. dedicated instances)
            if 'provider' in svc_data and 'provider' in svc_settings:
                print('setting provider...')
                set_provider_response = setServiceProvider(serverName, serverPort, token, folder_name, service_name, svc_settings['provider'])

                print('set provider response: {}'.format(set_provider_response))





