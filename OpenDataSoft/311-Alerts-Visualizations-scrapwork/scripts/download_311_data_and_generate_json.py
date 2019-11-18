import requests, json, os, shutil, sys, datetime, decimal

# returns the number of hours between two (int) Unix timestamps
def hours_between_timestamps(start, end):
    delta = end - start
    hours = float(delta)/3600
    # print(hours)
    return hours

# converts a unix timestamp to a human readable string in the local timezone
def timestamp_to_date_str(timestamp):
    lt = datetime.datetime.fromtimestamp(timestamp)
    return_str = str(lt.month) + '/' + str(lt.day) + '/' + str(lt.year)
    return return_str

'''
for every key in totals, store totals[key] / counts[key] in
averages[key]
'''
def calculate_averages(averages, counts, totals):
    for key in totals:
        val = totals[key]
        avg = round(float(val)/float(counts[key]), 3)
        averages[key] = avg

# return the sorted hash 'input_hash'
def sort_dict(input_hash):
    sorted_hash = {}
    for key in sorted(input_hash):
        # convert the key to a string first so that it matches the php result
        sorted_hash[str(key)] = input_hash[key]
    return sorted_hash


workspace = r'\\vgisdev\apps\visualizations\QAlerts-scrapwork\json'

# POST request
dataParams = {
    'dataset':'311-alerts-qscend',
    'format':'json'
}
# p = requests.post('https://cityofsalinas.opendatasoft.com/api/records/1.0/download/', data=dataParams)

# json_data = json.loads(p.text)

if not os.path.exists(workspace):
    os.makedirs(workspace)

json_file_path = workspace + r'\311-data.json'

json_data = None

with open(json_file_path) as json_file:
    json_data = json.load(json_file)

# print(len(json_data))

department_freq = {}
district_freq = {}
typename_freq = {}
origin_freq = {}

# average requests per department
department_hours = {}
num_department_records_with_hours = {}
avg_department_hours = {}

# average requests per district
district_hours = {}
num_district_records_with_hours = {}
avg_district_hours = {}

# average requests per typename
typename_hours = {}
num_typename_records_with_hours = {}
avg_typename_hours = {}

# average requests per origin
origin_hours = {}
num_origin_records_with_hours = {}
avg_origin_hours = {}

# for department timeline
department_hash = []
department_types = []
department_datasets = {
    'dates': []
}

# for district timeline
district_hash = []
district_types = []
district_datasets = {
    'dates': []
}

# for typename timeline
typename_hash = []
typename_types = []
typename_datasets = {
    'dates': []
}

# for origin timeline
origin_hash = []
origin_types = []
origin_datasets = {
    'dates': []
}

# request code counts
open_requests = 0
closed_requests = 0
in_progress_requests = 0
on_hold_requests = 0

for record in json_data:
    try:
        department = record['fields']['dept']
    except:
        department = None
    try:
        district = record['fields']['district']
    except:
        district = None
    try:
        typename = record['fields']['typename']
    except:
        typename = None
    try:
        ts_closed = int(record['fields']['dateclosedunix'])
    except:
        ts_closed = None
    try:
        ts_added = int(record['fields']['adddateunix'])
    except:
        ts_added = None
    try:
        record_id = record['fields']['id']
    except:
        record_id = None
    hours_between = None
    try:
        request_status = record['fields']['status']
    except:
        request_status = None
    try:
        origin = record['fields']['origin']
    except:
        origin = None

    # print(department)
    # print(district)
    # print(typename)
    # print(ts_closed)
    # print(ts_added)
    # print(record_id)
    # print(hours_between)
    # print(request_status)
    # print(origin)

    if request_status == 0:
        open_requests += 1
    elif request_status == 1:
        closed_requests += 1
    elif request_status == 3:
        in_progress_requests += 1
    elif request_status == 4:
        on_hold_requests += 1
    else:
        print('Unknown Request Type.')

    if ts_closed and ts_added:
        hours_between = hours_between_timestamps(ts_added, ts_closed)

    if department:
        if not department in department_freq:
            department_freq[department] = 0
        department_freq[department] += 1

    if district:
        if not district in district_freq:
            district_freq[district] = 0
        district_freq[district] += 1

    if typename:
        if not typename in typename_freq:
            typename_freq[typename] = 0
        typename_freq[typename] += 1

    if origin:
        if not origin in origin_freq:
            origin_freq[origin] = 0
        origin_freq[origin] += 1

    # get information for department timeline
    if ts_added and department:
        department_hash.append({
            'id' : record_id,
            'date_start' : timestamp_to_date_str(ts_added),
            'department' : department
        })
        if not department in department_types:
            department_types.append(department)

    # get information for district timeline
    if ts_added and district:
        district_hash.append({
            'id' : record_id,
            'date_start' : timestamp_to_date_str(ts_added),
            'district' : district
        })
        if not district in district_types:
            district_types.append(district)

    # get information for typename timeline
    if ts_added and typename:
        typename_hash.append({
            'id' : record_id,
            'date_start' : timestamp_to_date_str(ts_added),
            'typename' : typename
        })
        if not typename in typename_types:
            typename_types.append(typename)

    # get information for origin timeline
    if ts_added and origin:
        origin_hash.append({
            'id' : record_id,
            'date_start' : timestamp_to_date_str(ts_added),
            'origin' : origin
        })
        if not origin in origin_types:
            origin_types.append(origin)

    if department and ts_closed and ts_added:
        if not department in department_hours:
            department_hours[department] = 0
        if not department in num_department_records_with_hours:
            num_department_records_with_hours[department] = 0
        department_hours[department] += hours_between
        num_department_records_with_hours[department] += 1

    if district and ts_closed and ts_added:
        if not district in district_hours:
            district_hours[district] = 0
        if not district in num_district_records_with_hours:
            num_district_records_with_hours[district] = 0
        district_hours[district] += hours_between
        num_district_records_with_hours[district] += 1

    if typename and ts_closed and ts_added:
        if not typename in typename_hours:
            typename_hours[typename] = 0
        if not typename in num_typename_records_with_hours:
            num_typename_records_with_hours[typename] = 0
        typename_hours[typename] += hours_between
        num_typename_records_with_hours[typename] += 1

    if origin and ts_closed and ts_added:
        if not origin in origin_hours:
            origin_hours[origin] = 0
        if not origin in num_origin_records_with_hours:
            num_origin_records_with_hours[origin] = 0
        origin_hours[origin] += hours_between
        num_origin_records_with_hours[origin] += 1

# calculate averages
calculate_averages(avg_department_hours, num_department_records_with_hours, department_hours)
calculate_averages(avg_district_hours, num_district_records_with_hours, district_hours)
calculate_averages(avg_typename_hours, num_typename_records_with_hours, typename_hours)
calculate_averages(avg_origin_hours, num_origin_records_with_hours, origin_hours)

# sort hash tables
department_freq = sort_dict(department_freq)
department_hours = sort_dict(department_hours)
avg_department_hours = sort_dict(avg_department_hours)
department_datasets = sort_dict(department_datasets)
district_freq = sort_dict(district_freq)
district_hours = sort_dict(district_hours)
avg_district_hours = sort_dict(avg_district_hours)
district_datasets = sort_dict(district_datasets)
typename_freq = sort_dict(typename_freq)
typename_hours = sort_dict(typename_hours)
avg_typename_hours = sort_dict(avg_typename_hours)
typename_datasets = sort_dict(typename_datasets)
origin_freq = sort_dict(origin_freq)
origin_hours = sort_dict(origin_hours)
avg_origin_hours = sort_dict(avg_origin_hours)
origin_datasets = sort_dict(origin_datasets)

request_status_freq = {
    'Open' : open_requests,
    'Closed' : closed_requests,
    'In-Progress' : in_progress_requests,
    'On-Hold' : on_hold_requests
}

json_result = {
    'requestStatusFreq' : request_status_freq,
    'departmentFreq' : department_freq,
    'departmentHours' : department_hours,
    'avgDepartmentHours' : avg_department_hours,
    'departmentDatasets' : department_datasets,
    'districtFreq' : district_freq,
    'districtHours' : district_hours,
    'avgDistrictHours' : avg_district_hours,
    'districtDatasets' : district_datasets,
    'typenameFreq' : typename_freq,
    'typenameHours' : typename_hours,
    'avgTypenameHours' : avg_typename_hours,
    'typenameDatasets' : typename_datasets,
    'originFreq' : origin_freq,
    'originHours' : origin_hours,
    'avgOriginHours' : avg_origin_hours,
    'originDatasets' : origin_datasets,
    'numRecords' : len(json_data),
    'openRequests' : open_requests,
    'closedRequests' : closed_requests,
    'inProgressRequests' : in_progress_requests,
    'onHoldRequests' : on_hold_requests
}

# with open(json_file_path, 'w') as file:
#     file.write(p.text)

with open(workspace + r'\visualization_data_cached.json', 'w') as outfile:
    json.dump(json_result, outfile)

with open(r'\\vgisdev\apps\visualizations\QAlerts-scrapwork\scripts\output.json') as php_result:
    json_from_php = json.load(php_result)

    for key in json_result:
        if json_from_php[key] != json_result[key]:
            print(key)
            # print(json_from_php[key])
            # print(json_result[key])
            # print('')

    print('')
    dataset_name = 'avgTypenameHours'
    print(dataset_name)

    # print(json_from_php[dataset_name])
    # print(json_result[dataset_name])

    for key in json_from_php[dataset_name]:
        if json_from_php[dataset_name][key] != json_result[dataset_name][key]:
            print(key)
            print(json_from_php[dataset_name][key])
            print(json_result[dataset_name][key])


