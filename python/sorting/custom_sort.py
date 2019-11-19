import datetime, functools

def date_compare(a, b):
    a = a['date_start']
    b = b['date_start']
    delta = datetime.datetime.strptime(a, '%m/%d/%Y') - datetime.datetime.strptime(b, '%m/%d/%Y')
    return delta.total_seconds()

data = [
    {'id': 444, 'date_start': '2/22/2018', 'department': 'PWK-MAINT SVCS'},
    {'id': 444, 'date_start': '3/22/2018', 'department': 'PWK-MAINT SVCS'},
    {'id': 444, 'date_start': '2/23/2018', 'department': 'PWK-MAINT SVCS'},
    {'id': 444, 'date_start': '1/22/2018', 'department': 'PWK-MAINT SVCS'},
    {'id': 444, 'date_start': '2/24/2018', 'department': 'PWK-MAINT SVCS'},
    {'id': 444, 'date_start': '3/22/2018', 'department': 'PWK-MAINT SVCS'},
    {'id': 444, 'date_start': '2/22/2018', 'department': 'PWK-MAINT SVCS'},
    {'id': 444, 'date_start': '1/26/2018', 'department': 'PWK-MAINT SVCS'},
    {'id': 444, 'date_start': '2/28/2018', 'department': 'PWK-MAINT SVCS'}
]

sorted_data = sorted(data, key=functools.cmp_to_key(date_compare))

for item in data:
    print(item)

print('')

for item in sorted_data:
    print(item)