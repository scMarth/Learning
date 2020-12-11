import arcpy, json, os, sys

fc = r"D:\TEST_CONNECTION\TEST.sde\LINES"

field_data = arcpy.ListFields(fc)

field_index_lookup = {}

for i in range(len(field_data)):
    field = field_data[i].name
    field_index_lookup[i] = field

for key in sorted(field_index_lookup):
    print('{} : {}'.format(key, field_index_lookup[key]))

print('\nfield names:')
for field in field_data:
    print('{}'.format(field.name))
print('')

for field in field_data:
    print('field name: {}'.format(field.name))
    print('field domain: {}'.format(field.domain))
    print('')

with arcpy.da.SearchCursor(fc, '*') as cursor:
    count = 0
    for row in cursor:
        print('')
        for i in range(len(row)):
            val = row[i]
            field_name = field_index_lookup[i]

            print('{} : {}'.format(field_name, val))

        count += 1
        if count == 10:
            break