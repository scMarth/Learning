import requests

r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?&address=salinas%20home%20depot', auth=('user','pass'))
print("Status Code:\n")
print(r.status_code)
print("\nOutput:\n")
print(r.text)
