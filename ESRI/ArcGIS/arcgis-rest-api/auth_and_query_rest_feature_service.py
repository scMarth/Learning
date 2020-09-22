import requests, sys, json

def get_token(username, password, protocol, rest_server_host):
    token_url = "{protocol}{host}/server/tokens/".format(
        protocol=protocol,
        host=rest_server_host
    )

    params = {
        'username': username,
        'password': password,
        "client": "requestip", # for some reason, ip or using referer doesn't work
        'f': 'json'
        # 'expiration': 5 # let's not specify the expiration and have it use the default expiration time
    }

    response = requests.post(token_url, params)

    if response.status_code == 200:
        return response.json()['token']
    else:
        print('An error occurred while trying to get access token. Aborting.')
        sys.exit()

def get_record_count(protocol, rest_server_host, layer_query_url, token):
    url = "{protocol}{host}{layer_query_url}".format(
        protocol=protocol,
        host=rest_server_host,
        layer_query_url=layer_query_url
    )

    params = {
        'where': '1=1',
        'token': token,
        'returnCountOnly': True,
        'f': 'json'
    }

    print('url: {}'.format(url))

    response = requests.post(url, params)
    print(response.status_code)
    print(response.text)


    if response.status_code == 200:
        return json.loads(response.text)['count']
    else:
        print('An error occurred while trying to get access token. Aborting.')
        sys.exit()


username = ""
password = ""
protocol = "https://"
rest_server_host = "some.hostname.com"

token = get_token(username, password, protocol, rest_server_host)
print(token)

layer_query_url = r'/server/rest/services/FOLDER/SERVICE_NAME/FeatureServer/2/query'

feature_count = get_record_count(protocol, rest_server_host, layer_query_url, token)
print('feature count: {}'.format(feature_count))