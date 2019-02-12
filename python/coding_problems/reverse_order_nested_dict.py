# https://stackoverflow.com/questions/54634099/how-to-reverse-order-nested-dictionary-in-python3/54635085#54635085

import json, collections

existing = {
    "Entries": {
        "2019/01/23": {
            "Result-9595905890": {
                "count": 4,
                "time": "2019/01/23 03:32:32"
            }
        },
        "2019/01/24": {
            "Result-9607169713": {
                "count": 21,
                "time": "2019/01/24 03:31:34"
            },
            "Result-9611777668": {
                "count": 23,
                "time": "2019/01/24 12:58:49"
            }
        },
        "2019/01/25": {
            "Result-9618433556": {
                "count": 21,
                "time": "2019/01/25 03:31:27"
            }
        }
    }
}

new_entries = collections.OrderedDict(reversed(sorted(existing['Entries'].items()))) # if you want reversed sorted
existing['Entries'] = new_entries

with open('Entries.json', 'w') as outfile:
    json.dump(existing, outfile, indent=4)