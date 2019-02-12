# https://stackoverflow.com/questions/54523847/how-to-create-a-dictionary-from-a-txt-file-on-python

myDict = {}

with open('dict.txt', 'r') as file:
    for line in file:
        key, value = line.strip().split(':')
        myDict[key] = value

print myDict