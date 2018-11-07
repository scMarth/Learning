listy = ["A", "C", "D", "E", "F", "Z", "L", "K"]
print(listy)
listy.reverse() # this does an in-place reversal, and returns None
print(listy)

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

print("\nReversed:\n")

# this will work because reversed() returns an iterator
# you can't do sorted(hashmap, key=lambda k: hashmap[k]).reverse() because
# reverse() returns None and only does an in-place reversal
for key in reversed(sorted(hashmap, key=lambda k: hashmap[k])):
   print(key + " : " + str(hashmap[key]))

'''

alternatively, we could have done:

for key in sorted(hashmap, key=lambda k: hashmap[k], reverse=True):

'''