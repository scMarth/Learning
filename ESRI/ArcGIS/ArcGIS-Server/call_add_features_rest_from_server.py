# assumes that the machine running the script is an ArcGIS Server that hosts ArcGIS REST Services
# script will use addFeatures to create multiple polygon features

import arcpy, os, requests, urllib, json, sys, datetime


if environment == "DEV":
    connection = r"D:\DatabaseConnection\DEV.sde\TEST_DB.SCRAPWORK."
    layer_url = r'/rest/services/FOLDER/TEST_SERVICE/FeatureServer/2/addFeatures'
elif environment == "TEST":
    connection = r"D:\DatabaseConnection\TEST.sde\TEST_DB.SCRAPWORK."
    layer_url = r'/rest/services/FOLDER/TEST_SERVICE/FeatureServer/2/addFeatures'
elif environment == "STAGE" or environment == "STG" or environment == "STAGING":
    connection = r"D:\DatabaseConnection\STAGE.sde\TEST_DB.SCRAPWORK."
    layer_url = r'/rest/services/FOLDER/TEST_SERVICE/FeatureServer/2/addFeatures'
elif environment == "PROD" or "Prod":
    connection = r"D:\DatabaseConnection\PROD.sde\TEST_DB.SCRAPWORK."
    layer_url = r'/rest/services/FOLDER/TEST_SERVICE/FeatureServer/2/addFeatures'

# get access token from the arcgis rest server
def get_token(username, password, protocol, arcgis_server_url):

    token_url = "{protocol}{host}".format(
        protocol=protocol,
        host=arcgis_server_url
    ) + r'/tokens/generateToken'

    params = {
        'username': username,
        'password': password,
        "client": "requestip",
        'f': 'json'
    }

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    params = urllib.urlencode(params)

    response = requests.post(token_url, data=params, headers=headers, verify=False)

    if response.status_code == 200:
        if 'token' in response.json():
            print('token:')
            print(response.json())
            return response.json()['token']
        else:
            error_msg = 'An error occurred while trying to create an access token. Check login info. Aborting.'
            print('Error: ' + error_msg)
            sys.exit()
    else:
        error_msg = 'An error occurred while trying to get access token. Aborting.'
        print('Error: ' + error_msg)
        sys.exit()

username = ''
password = ''
protocol = str("https://")
arcgis_server_url = r'localhost/server'

poly = {
    "rings" :
    [
        [
            [-121.59023328799998,36.690195286000062],
            [-121.59046949499998,36.69055669800008],
            [-121.59016395599997,36.690712191000046],
            [-121.58990671199996,36.690361708000069],
            [-121.59023328799998,36.690195286000062]
        ]
    ],
    "spatialReference" :
    {
        "wkid" : 4326,
        "latestWkid" : 4326
    }
}

parent_id = '{D59FB0E8-9ECD-4C92-B465-60E1BE89C375}'

features = []

for i in range(11, 21):

    # print(i)

    feature = {}

    feature['geometry'] = poly
    feature['attributes'] = {
        'NOTES' : 'python script test {}'.format(i),
        'PARENT_ID' : parent_id
    }

# print(features)

# attempt to acquire a token, timeout after 1 minute
token = None
token_acquired = False
begin_time = datetime.datetime.now()
curr_time = begin_time
while not token_acquired:
    curr_time = datetime.datetime.now()

    # timeout after 1 minute of trying to get token
    if curr_time - begin_time > datetime.timedelta(seconds = 20):
        break

    try:
        token = get_token(username, password, protocol, arcgis_server_url)
        if token:
            token_acquired = True
    except Exception as e:
        # arcpy.AddMessage('Error: {}'.format(e))
        # arcpy.AddMessage('Failed to acquire access token, retrying...')
        continue

if not token_acquired:
    print('Timed out trying to acquire token, please try agian later.')
    sys.exit()
else:
    print('token: {}'.format(token))

url = "{protocol}{host}{layer_query_url}".format(
    protocol=protocol,
    host=arcgis_server_url,
    layer_query_url=layer_url
)

params = {
    'features': json.dumps(features),
    'token': token,
    'f': 'json'
}

headers = {'Content-Type': 'application/x-www-form-urlencoded'}



response = requests.post(url, data=params, headers=headers, verify=False)

if response.status_code != 200:
    error_msg = 'Query request failed. Aborting.'
    print(error_msg)
    sys.exit()
else:
    data_obj = response.json()
    # arcpy.AddMessage(data_obj)

    try:
        if data_obj['addResults'][0]['success'] == False:
            error_msg = 'Query request failed. Aborting.'
            error_msg += '\n'
            error_msg += str(data_obj)
            print(error_msg)
            sys.exit()
        else:
            print('request done:')
            print(data_obj)
    except:
        error_msg = 'Query request failed. Aborting.'
        error_msg += '\n'
        error_msg += str(data_obj)
        print(error_msg)
        sys.exit()