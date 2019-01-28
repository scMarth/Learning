import itertools
combs = ['AA','BB','C','X', 'X'] # i grouped AA becouse they are grouped and "X" = None

mylist = sorted(list(itertools.permutations(combs))) #create all possible permutations

#split the groups
tuppleSet = set()
for line in mylist:
    t = ()
    for string in line:
        string.split("\\")
        t = t + tuple(string)
    tuppleSet.add(t)

newlist = sorted(tuppleSet)
for line in newlist:
    if line[0] == "C" or line[0] == "X" and line[1] == "A" or line[1] == "B": #restricton with table size 
        continue
    elif line[6] == "X" or line[6] == "C" and line[4] == "A" or line[4] == "B": #restricton with table size 
        continue
    print(line)
