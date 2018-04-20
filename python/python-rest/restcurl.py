# test : https://notebooks.esri.com/

import requests

r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?&address=610%20COLLEGE%20DR%20%20salinas&key=AIzaSyDvpdRhA70xZXiipApEbXkZh5wYbF4zFIw')
print("r.json():\n\n" + str(r.json()) + "\n")

print(r.json()['results'][0]['address_components'][0]['long_name'])
