import csv

new_entry = [('Dolan','Tromp', 'Orange')]

with open(r'./example.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerows(new_entry)

'''
note that writerows in Windows writes both 0x0D 0x0D 0x0A so if the file
is opened in sublime, it will look like there are multiple newlines
'''


with open(r'./example.csv', 'rb') as file:
    reader = csv.reader(file)
    header = reader.next()
    table = [row for row in header]

    print(header)
    print(table)
