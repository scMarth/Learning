import requests

url = "https://your.agol.url.com/sharing/generateToken"

payload='f=json&username=USERNAME&password=PASSWORD&client=requestip'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
