# https://stackoverflow.com/questions/54369870/python-combination-without-repetition-with-sublists-items

import itertools, sys

# people = ['A', 'A', 'B', 'B', 'C']
# rooms = [2, 3, 2]
people = ['A', 'A', 'B', 'B', 'B', 'C']
rooms = [2, 3, 2, 3]

if len(people) > sum(rooms):
    print("Too much people for rooms.")
    sys.exit()

combs = []

for key, group in itertools.groupby(people):
    combs.append(key * len(list(group)))

for _ in range(0, sum(rooms) - len(people)):
    combs.append('X')

mylist = sorted(list(itertools.permutations(combs))) #create all possible permutations

unique_assignments = []

# test if two assignemtns are equivalent
def equivalent_assignments(assignment1, assignment2):
    for i in range(0, len(assignment1)):
        if tuple(assignment1[i]) not in itertools.permutations(assignment2[i]):
            return False
    return True

# for every permutation
for line in mylist:
    fits = True
    rooms_ind = 0
    comb_ind = 0

    room = rooms[rooms_ind]
    comb = line[comb_ind]

    room_assignments = []
    room_assignment = []

    # see if this permutation will fit
    while True:
        if room < len(comb):
            break
        elif room == len(comb):
            comb_ind += 1
            rooms_ind += 1
            room_assignment.append(comb)
            room_assignments.append(room_assignment)
            room_assignment = []
            try:
                room = rooms[rooms_ind]
                comb = line[comb_ind]
            except:

                break
        else: # room > len(comb)
            room_assignment.append(comb)
            room -= len(comb)
            comb_ind += 1
            try:
                comb = line[comb_ind]
            except:
                break

    # if we have leftover people, they don't fit
    if comb_ind < len(line) - 1:
        fits = False

    # check for same assignments
    if fits:
        same_assignments = [x for x in unique_assignments if equivalent_assignments(x, room_assignments)]
        if len(same_assignments) == 0:
            unique_assignments.append(room_assignments)

# print results
for line in unique_assignments:
    print line