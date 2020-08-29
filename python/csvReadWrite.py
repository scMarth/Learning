import csv, codecs

new_entries = [
    ('Cherry','MX','Brown'),
    (u'Marias De San Jer\xf3nimo', 'Test', 4)
]

'''
with open(r'./example.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerows(new_entry)
'''

# works in python 2.7.16
with open(r'./example.csv', 'a') as file:
    writer = csv.writer(file)
    
    for row in new_entries:

        insert = []

        for x in row:
            if isinstance(x, unicode):
                insert.append(x.encode('utf-8'))
            else:
                insert.append(x)

        writer.writerow(insert)

'''
# this doesn't work in python 2.7.16
with codecs.open(r'./example.csv', 'a', encoding='utf8') as file:
    writer = csv.writer(file)
    writer.writerows(new_entries)
'''
'''
note that writerows in Windows writes both 0x0D 0x0D 0x0A so if the file
is opened in sublime, it will look like there are multiple newlines
'''

'''
with open(r'./example.csv', 'rb') as file:
    reader = csv.reader(file)
    header = reader.next()
    table = [row for row in header]

    print(header)
    print(table)
'''
