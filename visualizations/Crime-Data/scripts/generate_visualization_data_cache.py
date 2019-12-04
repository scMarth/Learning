import arcpy, sys, datetime

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
print(field_to_index_map)
print('')

num_records = len(crime_data_hash)

print('{} records loaded into memory'.format(num_records))
print('')


# records_to_process = 10
# records_processed = 0

num_gang_related_records = 0
num_non_gang_related_records = 0

gang_related_types = []

for objid in crime_data_hash:
    record = crime_data_hash[objid]

    gang_related = record[field_to_index_map['GangRpt']]
    start_date = record[field_to_index_map['Occdate_On']]

    print(start_date)
    print(start_date.year)
    

    if gang_related == 'Y':
        num_gang_related_records += 1
    else:
        num_non_gang_related_records += 1

    if gang_related not in gang_related_types:
        gang_related_types.append(gang_related)

    # records_processed += 1
    # if records_processed == records_to_process:
    #     sys.exit()

    sys.exit()

print(gang_related_types)
print(num_gang_related_records)
print(num_non_gang_related_records)