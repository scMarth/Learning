import json, sys

json_1 = r"M:\GIS_Projects\Qscend\request_data\response_with_date_closed.json"
json_2 = r'\\vgisdev\apps\visualizations\QAlerts\json\311-data.json'

json_data_1 = None
json_data_2 = None

# load the json
with open(json_1) as json_file:
    json_data_1 = json.load(json_file)['request']

with open(json_2) as json_file:
    json_data_2 = json.load(json_file)

# compare the lengths of the datasets
if len(json_data_1) != len(json_data_2):
    print('Uneven lengths. Aborting.')
    sys.exit()
else:
    print('Both length {}'.format(len(json_data_1)))

# create hashes and objid list
objid_list = []
json_data_1_hash = {}
json_data_2_hash = {}

ids = 0

for record in json_data_1:
    objid = record['id']
    objid_list.append(objid)
    json_data_1_hash[objid] = record

for record in json_data_2:
    objid = record['fields']['id']
    json_data_2_hash[objid] = record

objid_list = sorted(objid_list)

# create list of objids where the respective records differ
diff_hash = {}
diff_objids = []
for objid in objid_list:
    record_1 = json_data_1_hash[objid]
    record_2 = json_data_2_hash[objid]['fields']

    diff_key_list = []

    for key in record_1:
        if key.lower() in record_2:
            if record_2[key.lower()] != record_1[key]:
                if key in ['displayDate', 'displayLastAction', 'comments', 'displayDateClosed', 'privateNotes']:
                    continue
                else:
                    if key in ['addDateUnix', 'lastActionUnix', 'dateClosedUnix']:
                        if record_1[key] != int(record_2[key.lower()]):
                            diff_key_list.append(key)
                    elif key in ['district']:
                        if int(record_1[key]) != record_2[key.lower()]:
                            diff_key_list.append(key)
                    else:
                        diff_key_list.append(key)

    if diff_key_list:
        diff_objids.append(objid)
        diff_hash[objid] = diff_key_list

print('Number of records that differ from one dataset to another: {}\n'.format(len(diff_objids)))

for objid in diff_objids:
    record_1 = json_data_1_hash[objid]
    record_2 = json_data_2_hash[objid]['fields']

    diff_key_list = diff_hash[objid]

    # print('id: {}'.format(objid))
    print(diff_key_list)

    for key in diff_key_list:
        # print('1. {} : {} ; {}'.format(key, record_1[key], type(record_1[key])))
        # print('2. {} : {} ; {}'.format(key, record_2[key.lower()], type(record_2[key.lower()])))
        # print('')

        obj_1 = record_1[key]
        obj_2 = record_2[key.lower()]

        obj_1 = obj_1.split()
        obj_1 = (' ').join(obj_1)

        if obj_1 == obj_2:
            # print('removed whitespace')
            continue
        else:
            print('still diff')