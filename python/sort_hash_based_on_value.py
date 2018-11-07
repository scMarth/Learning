hashmap = { \
   "A" : 120, \
   "B" : 8, \
   "C" : 87, \
   "D" : 54, \
   "E" : 45, \
   "F" : 20, \
   "G" : 58, \
   "H" : 0, \
   "I" : 9, \
   "J" : 2, \
   "K" : 45, \
   "L" : 12, \
   "M" : 132, \
   "N" : 112 \
}

for key in sorted(hashmap, key=lambda k: hashmap[k]):
   print(key + " : " + str(hashmap[key]))