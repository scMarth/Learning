import arcpy, requests, sys, datetime, os, csv, shutil, logging, json

logging.basicConfig(filename=r'C:\logs\addFeaturesLog.txt', level=logging.WARN, format='%(asctime)s %(message)s')

username = "username"
password = "password"

arcgis_server_url = r'test-url.com/server'
layer_query_url = r'/rest/services/TEST/Service_Name/FeatureServer/0/query'

# get access token from the arcgis rest server
def get_token(username, password, protocol, arcgis_server_url):
    token_url = "{protocol}{host}/tokens/".format(
        protocol=protocol,
        host=arcgis_server_url
    )

    params = {
        'username': username,
        'password': password,
        "client": "requestip",
        'f': 'json'
    }

    response = requests.post(token_url, params)

    if response.status_code == 200:
        if 'token' in response.json():
            return response.json()['token']
        else:
            print_and_log('An error occurred while trying to create an access token. Check login info. Aborting.', True, True)
            print_and_log('response: {}'.format(response.json()), True, True)
            sys.exit()
    else:
        print_and_log('An error occurred while trying to get access token. Aborting.', True, True)
        sys.exit()

def print_and_log(input_str, print_flag, log_flag):
    if print_flag:
        print(input_str)
    if log_flag:
        logging.warning(input_str.rstrip())

# get the number of features in the feature service layer
def get_record_count(protocol, arcgis_server_url, layer_query_url, token):
    url = "{protocol}{host}{layer_query_url}".format(
        protocol=protocol,
        host=arcgis_server_url,
        layer_query_url=layer_query_url
    )

    params = {
        'where': '1=1',
        'token': token,
        'returnCountOnly': True,
        'f': 'json'
    }

    response = requests.post(url, params)

    if response.status_code == 200:
        if 'count' in response.json():
            return response.json()['count']
        else:
            print_and_log('An error occurred while trying to get the feature count. Aborting.', True, True)
            print_and_log('response: {}'.format(response.json()), True, True)
            sys.exit()
    else:
        print_and_log('An error occurred while trying to get access token. Aborting.', True, True)
        sys.exit()

# create and return a polygon based on multipolygon rings returned from REST service
def get_polygon_from_rings(rings):

    array = arcpy.Array()

    for ring in rings:
        sub_array = arcpy.Array()

        for coords in ring:
            x, y = coords
            pnt = arcpy.Point(x,y)
            sub_array.add(pnt)

        array.add(sub_array)

    sr = arcpy.SpatialReference(4326)
    polygon = arcpy.Polygon(array, sr)
    return polygon

def add_feature():
    global layer_query_url

    protocol = "https://"

    start_time = datetime.datetime.now()

    print_and_log('start time: {}\n'.format(start_time), True, True)

    print('layer_query_url: {}'.format(layer_query_url))

    # get an access token for the feature service
    token = get_token(username, password, protocol, arcgis_server_url)

    url = "{protocol}{host}{layer_query_url}".format(
        protocol=protocol,
        host=arcgis_server_url,
        layer_query_url=layer_query_url
    )

    features = []

    params = {
        'where': 'OBJECTID = 1',
        'token': token,
        'f': 'json',
        'geometryType': 'esriGeometryPolygon',
        'spatialRel': 'esriSpatialRelIntersects',
        'outFields': '*',
        'returnGeometry': 'true'
    }

    response = requests.post(url, params)
    print_and_log('\tResponse status: {}'.format(response.status_code), True, False)

    if response.status_code != 200:
        print_and_log('Query request failed. Aborting.', True, True)
        sys.exit()
    else:
        data_obj = response.json()

        print('data_obj:')
        print(data_obj)

        num_returned_features = len(data_obj['features'])
        print('num_returned_features: {}'.format(num_returned_features))


        for feature in data_obj['features']:
            features.append(feature)
        

    print('outside loop:')
    print(features[0])

    send_feature = features[0]

    send_feature['attributes']['NOTES'] = 'The quick brown fox'

    print('')
    print(send_feature)

    del(send_feature['attributes']['OBJECTID'])

    print('')
    print(send_feature)

    layer_query_url = r'/rest/services/TEST/Service_Name/FeatureServer/0/addFeatures'

    # get an access token for the feature service
    token = get_token(username, password, protocol, arcgis_server_url)

    url = "{protocol}{host}{layer_query_url}".format(
        protocol=protocol,
        host=arcgis_server_url,
        layer_query_url=layer_query_url
    )

    params = {
        'features': json.dumps(features),
        'token': token,
        'f': 'json'
    }

    print('')
    print('posting:')

    response = requests.post(url, params)
    print_and_log('\tResponse status: {}'.format(response.status_code), True, False)

    if response.status_code != 200:
        print_and_log('Query request failed. Aborting.', True, True)
        sys.exit()
    else:
        data_obj = response.json()

        print('data_obj:')
        print(data_obj)

    end_time = datetime.datetime.now()
    print_and_log('end time: {}'.format(end_time), True, True)
    print_and_log('time elapsed: {}\n'.format(end_time - start_time), True, False)

if __name__ == '__main__':
    print('layer_query_url: {}'.format(layer_query_url))
    add_feature()