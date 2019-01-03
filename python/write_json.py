import json

json_obj = ['key', {'inner key' : (1, 2, 3, 4, 5)}]

print(json.dumps(json_obj))