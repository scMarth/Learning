# https://stackoverflow.com/questions/54525457/problem-counting-lines-in-csv-file-with-python#54525457

with open('headerOnly.csv', mode='rb') as csv_file:
    #check for empty files 
    line_count =  sum(1 for line in csv_file)
    print(line_count)
    if line_count == 0:
        print("csv file is empty")
    elif line_count == 1:
        print("only has header")