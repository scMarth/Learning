import csv, os

book_list_path = os.path.dirname(os.path.abspath(__file__)) + '/Book-List2.csv'

rows = []

with open(book_list_path, 'r', newline='') as csvfile:
   csvreader = csv.reader(csvfile) 
   for row in csvreader:
      if csvreader.line_num > 1:
         rows.append(row)

rows.sort(key=lambda x: (x[1], x[0]))

with open(book_list_path, 'w', newline='', encoding='utf-8') as csvfile:
   csvwriter = csv.writer(csvfile, lineterminator='\n')
   csvwriter.writerow(['Title', 'Author'])
   for row in rows:
      csvwriter.writerow(row)


