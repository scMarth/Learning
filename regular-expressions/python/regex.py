'''

https://www.regular-expressions.info

tests in python 2.7.10

'''

import re

match = re.search("the", "the ether etheo eth thathe the")
print(match.group(0))

match = re.findall("the", "the ether etheo eth thathe the")
print(match)

matches = re.findall("the", "the ether etheo eth thathe the")
print("len matches: " + str(len(matches)))
for m in matches:
    print(m)

# character class subtraction, not supported apparently
matches = re.findall("[0-9-[1-3]]", "3457193846081-7830-54586avaaavioertuqvetsdrtvldyhtgsletaiuet")
for m in matches:
    print(m)

print("Character Class Intersections")
# character class intersection, not supported apparently
matches = re.findall("[0-9&&0-1]","9 4 3 1 2 3 4 5 6 8 7 6 5 4 2 1")
for m in matches:
    print(m)

print("Word Boundaries")
matches = re.findall("\\bthe\\b", "the ether etheo eth thathe the")
for m in matches:
    print(m)

print("Alternation")
matches = re.findall("the|dog", "the quick brown fox jumps over the lazy dog")
for m in matches:
    print(m)

# not supported apparently, works in Sublime regex search
print("Optional Items")
matches = re.findall("Nov(ember)?", "November Dec December Nov February")
for m in matches:
    print(m)
    
# not supported apparently, works in Sublime regex search
print("Backreferences")
matches = re.findall("(Nov)x\1\1", "NovxNovNov Nov x Nov NovxNovxNovNov")
for m in matches:
    print(m)
