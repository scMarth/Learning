some_list = [
   [1, 4, 'a'],
   [2, 23, 'a'],
   [3, 5, 'a'],
   [4, 7, 'a'],
   [4, 8, 'a'],
   [4, 7, 'a'],
   [4, 5, 'a'],
   [5, 9, 'a'],
   [5, 1, 'a'],
   [5, 4, 'a'],
   [6, 2, 'a'],
   [7, 3, 'a'],
   [5, 78, 'a'],
   [5, 6, 'a'],
   [3, 45, 'a'],
   [3, 2, 'a'],
   [1, 2, 'a'],
   [0, 1, 'a'],
   [0, 1, 'b'],
   [0, 1, 'z'],
   [0, 1, 'd'],
   [0, 1, 'a']
]

some_list.sort()

for item in some_list:
   print(item)

'''

by default, it seems that if you sort a list of lists, it sorts first by
sublist[0], then by sublist[1] ... sublist[n]

'''