import os, requests, urllib, json, sys, datetime, time, socket


username = ''
password = ''
protocol = str("https://")



def print_and_log(msg):
    print(msg)
    with open(output_log, 'a') as file:
        file.write('{}\n'.format(msg))

workspace = os.path.dirname(os.path.abspath(__file__))
output_log = workspace + r'\referer_log.txt'

# delete output log if it exists
if os.path.exists(output_log):
    os.remove(output_log)


def get_token():

    # get a token
    get_token_url = "https://some.domain.com/arcgis/tokens/generateToken"
    payload = {
    'username' : username,
    'password' : password,
    # 'expiration': 60,
    # 'client' : 'requestip',
    'client': 'referer',
    'referer': 'https://some.domain.com',
    'f' : 'json'
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    payload = urllib.parse.urlencode(payload)

    response = requests.request("POST", get_token_url, headers=headers, data=payload)
    token = json.loads(response.text)['token']
    print_and_log('')
    print_and_log(str(datetime.datetime.now()) + ' : got token:')
    print_and_log(response.text)
    print_and_log('')
    return token



token = get_token()


count = 0
fail_count = 0

while True:
    update_url = "https://some.domain.com/arcgis/rest/services/FOLDER/SERVICE/FeatureServer/3/updateFeatures"

    expr =  [{
        "attributes": {
            "SURVEYOR": 'DEV_DEBUG',
            "OBJECTID": 20277331
        }
    }]

    payload = {
        'features': json.dumps(expr),
        'token': token,
        'f': 'json'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://some.domain.com'
    }


    payload = urllib.parse.urlencode(payload)
    response = requests.request("POST", update_url, headers=headers, data=payload)
    count += 1

    ip_addr = socket.gethostbyname(socket.gethostname())
    print_and_log('call {}: '.format(count) + 'ip: {} '.format(ip_addr) + str(datetime.datetime.now()) + ' : {}'.format(response.text) + ' : token={}'.format(token))
    response_data = json.loads(response.text)


    

    transaction_success = False

    try:
        # transaction_success = response_data['success']
        transaction_success = response_data['updateResults'][0]['success']
    except:
        transaction_success = False
        fail_count += 1

        # if the fail count reaches 5 with same token, get a new token
        if fail_count >= 5:
            fail_count = 0 # reset fail count
            token = get_token()

    # if not transaction_success:
    #     break


    # wait
    # time.sleep(300) # 300 seconds = 5 minutes
    time.sleep(5) # 5 seconds


print_and_log('\n' + str(datetime.datetime.now()) + ' : finished')