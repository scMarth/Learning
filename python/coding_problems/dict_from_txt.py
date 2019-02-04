myDict = {}

with open('dict.txt', 'r') as file:
    for line in file:
        key, value = line.strip().split(':')
        myDict[key] = value

print myDict