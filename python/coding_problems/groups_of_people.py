# https://stackoverflow.com/questions/54369870/python-combination-without-repetition-with-sublists-items

import itertools, sys

people = ['A', 'A', 'B', 'B', 'C']
rooms = [2, 3, 2]
# people = ['A', 'A', 'B', 'B', 'B', 'C']
# rooms = [2, 3, 2, 3]
# people = ['A', 'A', 'B', 'B', 'C', 'C', 'C', 'C', 'C'] # takes absurdly long
# rooms = [2, 3, 2, 5]

total_room_space = sum(rooms)
print("total_room_space: " + str(total_room_space))

people_padded = people
for i in range(0, (total_room_space - len(people))):
    people_padded.append('None')
print('people_padded: ' + str(people_padded))

unique_assignments = []

for perm in itertools.permutations(people_padded):
    perm_index = 0

    room_assignments = []
    for room_size in rooms:
        room_assignment = []
        for i in range(0, room_size):
            room_assignment.append(perm[perm_index])
            perm_index += 1
        room_assignments.append(tuple(room_assignment))

    skipflag = False

    # check for multiple rooms
    for room_assignment in room_assignments:
        rest = [x for x in room_assignments if x is not room_assignment]
        for room_asgn in rest:
            for code in room_assignment:
                if code != 'None':
                    if code in room_asgn:
                        skipflag = True

    # skip if needed
    if skipflag:
        continue

    if room_assignments not in unique_assignments:
        unique_assignments.append(room_assignments)

# return true if two room assignments are the same
def same_assignment(assignment1, assignment2):
    for i in range(0, len(assignment1)):
        if assignment1[i] not in itertools.permutations(assignment2[i]):
            return False
    return True

# clean up same combinations in unique_assignments
indeces = range(0, len(unique_assignments))
delete_indeces = []
while indeces:
    curr_index = indeces.pop(0)
    equivalent_assignments = [x for x in indeces if same_assignment(unique_assignments[x], unique_assignments[curr_index])]
    for ind in equivalent_assignments:
        delete_indeces.append(ind)
    indeces = [x for x in indeces if x not in equivalent_assignments]

for index in reversed(sorted(delete_indeces)):
    del unique_assignments[index]

# print results
print("\n\nResults:")
for assignment in unique_assignments:
    print assignment