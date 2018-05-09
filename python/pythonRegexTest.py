import re

# MAKE SURE TO CAST MULTISPACES TO SPACE

stringArray = ['A', 'C/A', 'BLDG A', 'UNIT A']

for string in stringArray:
   print(string + " | " + str(len(string.split())))

   if (len(string.split()) == 1):
      if (re.search('^[a-zA-Z0-9]+$', string)):
         print(string)
         print('\tUNIT ' + string)
         print('\tBLDG ' + string)
         print('\tPARCEL ' + string)

   print("")
