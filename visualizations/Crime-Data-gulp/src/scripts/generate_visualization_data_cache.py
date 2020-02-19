import arcpy, sys, datetime, functools, os, json

# converts a datetime to a human readable string
def dt_to_date_str(dt):
    return str(dt.month) + '/' + str(dt.day) + '/' + str(dt.year)

'''
for every key in totals, store totals[key] / counts[key] in
averages[key]
'''
def calculate_averages(averages, counts, totals):
    for key in totals:
        val = totals[key] 

        # avg = float(val)/float(counts[key])
        # # use Decimal to round exact halves up (python rounds down by default)
        # dec = decimal.Decimal(avg)
        # rounded = dec.quantize(decimal.Decimal(str(0.001)), rounding=decimal.ROUND_UP)
        # averages[key] = float(rounded)

        # avg = decimal.Decimal(str(val))/decimal.Decimal(str(counts[key]))
        # # use Decimal to round exact halves up (python rounds down by default)
        # rounded = avg.quantize(decimal.Decimal(str(0.001)), rounding=decimal.ROUND_UP)
        # averages[key] = float(rounded)

        avg = round(float(val)/float(counts[key]), 3)
        averages[key] = avg

# return the sorted hash 'input_hash'
def sort_dict(input_hash):
    sorted_hash = {}
    for key in sorted(input_hash):
        # convert the key to a string first so that it matches the php result
        sorted_hash[str(key)] = input_hash[key]
    return sorted_hash

# helper function for sort_month_year_keys_in_dict, compares dates in the form of month/year e.g. 4/2012
def month_year_compare(a, b):
    delta = datetime.datetime.strptime(a, '%m/%Y') - datetime.datetime.strptime(b, '%m/%Y')
    return delta.total_seconds()

# given an input hash with keys in the format month/year e.g. 4/2012, return a dict that is sotred in chronological order
def sort_month_year_keys_in_dict(input_hash):
    sorted_hash = {}
    sorted_hash_keys = sorted(input_hash, key=functools.cmp_to_key(month_year_compare))

    for month in sorted_hash_keys:
        sorted_hash[month] = input_hash[month]

    return sorted_hash

# format a month_year hash {'month/year':count} into {'dates': [], 'ylabel':[]}, in order to prepare them for the visualizations
def format_month_year_keys_for_json(input_hash, ylabel):
    yaxis = []
    dates = []

    for key in input_hash:
        dates.append(key)
        yaxis.append(input_hash[key])

    result = {'dates' : dates}
    result[ylabel] = yaxis

    return result

# return the sorted hash 'input_hash', keys must be ints or strings
def sort_dict_ints_and_str_keys(input_hash):
    sorted_hash = {}
    
    # find out which keys are strings and which are numbers
    num_keys = [] # keys that are numbers
    str_keys = [] # keys that are strings
    for key in input_hash:
        if isinstance(key, str):
            str_keys.append(key)
        elif isinstance(key, int) or isinstance(key, float):
            num_keys.append(key)

    # put in the number keys first in sorted order
    for key in sorted(num_keys):
        sorted_hash[str(key)] = input_hash[key]

    # put in the string keys next in sorted order
    for key in sorted(str_keys):
        sorted_hash[key] = input_hash[key]

    return sorted_hash

def date_compare(a, b):
    a = a['date_start']
    b = b['date_start']
    delta = datetime.datetime.strptime(a, '%m/%d/%Y') - datetime.datetime.strptime(b, '%m/%d/%Y')
    return delta.total_seconds()

def construct_dataset(datasets, keys, field, hash):
    prev_date = '';

    for key in keys:
        datasets[key] = []

    hash = sorted(hash, key=functools.cmp_to_key(date_compare))

    for record in hash:
        date_start = record['date_start']
        project_type = record[field]

        if date_start == prev_date:
            for key in datasets:
                if key == project_type:
                    datasets[key][-1] += 1
        else:
            for key in datasets:
                prev_date = date_start
                if key == 'dates':
                    datasets[key].append(date_start)
                elif key == project_type:
                    if len(datasets[key]) == 0:
                        datasets[key].append(1)
                    else:
                        lastVal = datasets[key][-1]
                        datasets[key].append(lastVal + 1)
                else:
                    if len(datasets[key]) == 0:
                        datasets[key].append(0)
                    else:
                        lastVal = datasets[key][-1]
                        datasets[key].append(lastVal)

# read crime data into memory from the holding directory
fc = r'M:\GIS_Projects\Public_Works\GIS_Division\crimeData\anonCrimeData.gdb\anonCrimeData'
crime_data_hash = {}
with arcpy.da.SearchCursor(fc, '*') as cursor:
    for row in cursor:
        objid = row[0]
        crime_data_hash[objid] = row

field_to_index_map = {}
index_count = 0
fields = arcpy.ListFields(fc)
for field in fields:
    print(field.name)
    field_to_index_map[field.name] = index_count
    index_count += 1
# print(field_to_index_map)
print('')

num_records = len(crime_data_hash)

print('{} records loaded into memory'.format(num_records))
print('')

arrest_made_freq = {}
gang_rpt_freq = {}
category_freq = {}
crime_desc_freq = {}
class_freq = {}
class_desc_freq = {}
beat_freq = {}
suspect_ages_freq = {}
victim_ages_freq = {}


# timeline for all crime
all_crime_hash = []
all_crime_types = ['crime'] # place a single crime as a placeholder for the crime type, since there is only one type
all_crime_datasets = {
    'dates': []
}

# for gang_rpt timeline
gang_rpt_hash = []
gang_rpt_types = []
gang_rpt_datasets = {
    'dates': []
}

# for category timeline
category_hash = []
category_types = []
category_datasets = {
    'dates': []
}

# for beat timeline
beat_hash = []
beat_types = []
beat_datasets = {
    'dates': []
}

# for arrest_made timeline
arrest_made_hash = []
arrest_made_types = []
arrest_made_datasets = {
    'dates': []
}

# for crime desc timeline
crime_desc_hash = []
crime_desc_types = []
crime_desc_datasets = {
    'dates': []
}

# for crimes per month timeline ; mapping from month to number of crimes in that month
crimes_per_month = {}

# for class timeline
class_hash = []
class_types = []
class_datasets = {
    'dates': []
}

# for class desc timeline
class_desc_hash = []
class_desc_types = []
class_desc_datasets = {
    'dates': []
}

# records_to_process = 10
# records_processed = 0

num_gang_related_records = 0
num_non_gang_related_records = 0

gang_related_types = []

total_records = 0

for objid in crime_data_hash:
    record = crime_data_hash[objid]

    total_records += 1

    gang_related = 'Y' if record[field_to_index_map['GangRpt']] == 'Y' else 'N'
    start_date = record[field_to_index_map['Occdate_On']]
    category = record[field_to_index_map['Category']]
    crime_description = record[field_to_index_map['Crime']]
    class_desc = record[field_to_index_map['Classdesc']]
    record_class = record[field_to_index_map['Class']]
    beat = record[field_to_index_map['Beat']]
    arrest_made = 'Y' if record[field_to_index_map['Arrest']] == 'Y' else 'N'
    victim_ages = record[field_to_index_map['VictAges']]
    suspect_ages = record[field_to_index_map['SuspectAge']]

    if victim_ages:
        orig = victim_ages
        victim_ages = victim_ages.split(',')
        for victim_age in victim_ages:
            age = int(victim_age.strip())

            if age > 200 or age < 0: # skip likely typos
                continue

            if age not in victim_ages_freq:
                victim_ages_freq[age] = 0
            victim_ages_freq[age] += 1

            # if age == 0 or age > 100 or age < 0:
            #     print(age)
            #     print(orig)
            #     print(victim_ages)
            #     print('')

    if suspect_ages:
        suspect_ages = suspect_ages.split(',')
        for suspect_age in suspect_ages:
            age = int(suspect_age.strip())

            if age > 200 or age < 0: # skip likely typos
                continue

            if age not in suspect_ages_freq:
                suspect_ages_freq[age] = 0
            suspect_ages_freq[age] += 1

    if arrest_made:
        if not arrest_made in arrest_made_freq:
            arrest_made_freq[arrest_made] = 0
        arrest_made_freq[arrest_made] += 1

    if not gang_related in gang_rpt_freq:
        gang_rpt_freq[gang_related] = 0
    gang_rpt_freq[gang_related] += 1

    if crime_description:
        if not crime_description in crime_desc_freq:
            crime_desc_freq[crime_description] = 0
        crime_desc_freq[crime_description] += 1

    if category:
        if not category in category_freq:
            category_freq[category] = 0
        category_freq[category] += 1

    if record_class:
        if not record_class in class_freq:
            class_freq[record_class] = 0
        class_freq[record_class] += 1

    if class_desc:
        if not class_desc in class_desc_freq:
            class_desc_freq[class_desc] = 0
        class_desc_freq[class_desc] += 1

    if beat:
        if not beat in beat_freq:
            beat_freq[beat] = 0
        beat_freq[beat] += 1

    if start_date:
        all_crime_hash.append({
            'id' : objid,
            'date_start' : dt_to_date_str(start_date),
            'crime' : 'crime'
        })
    
    # get information for crime per month timeline
    if start_date:
        month_key = str(start_date.month) + '/' + str(start_date.year)

        if month_key not in crimes_per_month:
            crimes_per_month[month_key] = 0

        crimes_per_month[month_key] += 1

    # get information for gang_rpt timeline
    if start_date:
        gang_rpt_hash.append({
            'id' : objid,
            'date_start' : dt_to_date_str(start_date),
            'gang_related' : gang_related
        })
        if not gang_related in gang_rpt_types:
            gang_rpt_types.append(gang_related)

    # get information for category timeline
    if start_date and category:
        category_hash.append({
            'id' : objid,
            'date_start' : dt_to_date_str(start_date),
            'category' : category
        })
        if not category in category_types:
            category_types.append(category)

    # get information for beat timeline
    if start_date and beat:
        beat_hash.append({
            'id' : objid,
            'date_start' : dt_to_date_str(start_date),
            'beat' : beat
        })
        if not beat in beat_types:
            beat_types.append(beat)

    # get information for crime_desc timeline
    if start_date:
        crime_desc_hash.append({
            'id' : objid,
            'date_start' : dt_to_date_str(start_date),
            'crime_desc' : crime_description
        })
        if not crime_description in crime_desc_types:
            crime_desc_types.append(crime_description)

    # get information for class timeline
    if start_date and record_class:
        class_hash.append({
            'id' : objid,
            'date_start' : dt_to_date_str(start_date),
            'class' : record_class
        })
        if not record_class in class_types:
            class_types.append(record_class)

    # get information for class_desc timeline
    if start_date and class_desc:
        class_desc_hash.append({
            'id' : objid,
            'date_start' : dt_to_date_str(start_date),
            'class_desc' : class_desc
        })
        if not class_desc in class_desc_types:
            class_desc_types.append(class_desc)

    # get information for arrest_made timeline
    if start_date and arrest_made:
        arrest_made_hash.append({
            'id' : objid,
            'date_start' : dt_to_date_str(start_date),
            'arrest_made' : arrest_made
        })
        if not arrest_made in arrest_made_types:
            arrest_made_types.append(arrest_made)


    if gang_related == 'Y':
        num_gang_related_records += 1
    else:
        num_non_gang_related_records += 1

    if gang_related not in gang_related_types:
        gang_related_types.append(gang_related)

    # records_processed += 1
    # if records_processed == records_to_process:
    #     sys.exit()

    # sys.exit()

# construct datasets
construct_dataset(all_crime_datasets, all_crime_types, 'crime', all_crime_hash)
construct_dataset(gang_rpt_datasets, gang_rpt_types, 'gang_related', gang_rpt_hash)
construct_dataset(category_datasets, category_types, 'category', category_hash)
construct_dataset(crime_desc_datasets, crime_desc_types, 'crime_desc', crime_desc_hash)
construct_dataset(class_datasets, class_types, 'class', class_hash)
construct_dataset(class_desc_datasets, class_desc_types, 'class_desc', class_desc_hash)
construct_dataset(beat_datasets, beat_types, 'beat', beat_hash)
construct_dataset(arrest_made_datasets, arrest_made_types, 'arrest_made', arrest_made_hash)

# sort hash tables
all_crime_datasets = sort_dict(all_crime_datasets)
gang_rpt_freq = sort_dict(gang_rpt_freq)
gang_rpt_datasets = sort_dict(gang_rpt_datasets)
category_freq = sort_dict(category_freq)
crime_desc_freq = sort_dict(crime_desc_freq)
category_datasets = sort_dict(category_datasets)
crime_desc_datasets = sort_dict(crime_desc_datasets)
class_freq = sort_dict(class_freq)
class_desc_freq = sort_dict(class_desc_freq)
class_datasets = sort_dict(class_datasets)
class_desc_datasets = sort_dict(class_desc_datasets)
beat_freq = sort_dict(beat_freq)
beat_datasets = sort_dict_ints_and_str_keys(beat_datasets)
arrest_made_freq = sort_dict(arrest_made_freq)
arrest_made_datasets = sort_dict(arrest_made_datasets)
suspect_ages_freq = sort_dict(suspect_ages_freq)
victim_ages_freq = sort_dict(victim_ages_freq)

# sort special hash tables with month/year keys
crimes_per_month = sort_month_year_keys_in_dict(crimes_per_month)

# format special month/year tables
crimes_per_month = format_month_year_keys_for_json(crimes_per_month, 'records')

json_result = {
    'crimesPerMonth' : crimes_per_month,
    'allCrimeDatasets' : all_crime_datasets,
    'gangRptFreq' : gang_rpt_freq,
    'gangRptDatasets' : gang_rpt_datasets,
    'categoryFreq' : category_freq,
    'categoryDatasets' : category_datasets,
    'crimeDescFreq' : crime_desc_freq,
    'crimeDescDatasets' : crime_desc_datasets,
    'classFreq' : class_freq,
    'classDescFreq' : class_desc_freq,
    'classDatasets' : class_datasets,
    'classDescDatasets' : class_desc_datasets,
    'beatFreq' : beat_freq,
    'beatDatasets' : beat_datasets,
    'arrestMadeFreq' : arrest_made_freq,
    'arrestMadeDatasets' : arrest_made_datasets,
    'suspectAgesFreq' : suspect_ages_freq,
    'victimAgesFreq' : victim_ages_freq,
    'numRecords' : total_records
}

workspace = r'\\vgisdev\apps\visualizations\Crime-Data\json'
# workspace = r'C:\inetpub\wwwroot\apps\visualizations\Crime-Data\json'
if not os.path.exists(workspace):
    os.makedirs(workspace)

with open(workspace + r'\visualization_data_cached.json', 'w') as outfile:
    json.dump(json_result, outfile)

# print(gang_related_types)
# print(num_gang_related_records)
# print(num_non_gang_related_records)