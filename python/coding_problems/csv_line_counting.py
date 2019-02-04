with open('headerOnly.csv', mode='rb') as csv_file:
    #check for empty files 
    line_count =  sum(1 for line in csv_file)
    print(line_count)
    if line_count == 0:
        print("csv file is empty")
    elif line_count == 1:
        print("only has header")