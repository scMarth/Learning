# https://stackoverflow.com/questions/54369870/python-combination-without-repetition-with-sublists-items
# incomplete

import itertools, sys

people = ['A', 'A', 'B', 'B', 'C']
rooms = [2, 3, 2]

total_room_space = sum(rooms)
print("total_room_space: " + str(total_room_space))

people_padded = people
for i in range(0, (total_room_space - len(people))):
    people_padded.append('None')

print('people_padded: ' + str(people_padded))

# get how many of each code there is
code_count = {}
for person_code in people:
    if person_code in code_count:
        code_count[person_code] += 1
    else:
        code_count[person_code] = 1
print code_count

# get list of unique codes
codes = []
for person_code in people:
    if person_code == 'None':
        continue
    if person_code not in codes:
        codes.append(person_code)
print("codes: " + str(codes))


unique_assignments = []

for perm in itertools.permutations(people_padded):
    perm_index = 0

    room_assignments = []
    for room_size in rooms:
        room_assignment = []
        for i in range(0, room_size):
            room_assignment.append(perm[perm_index])
            perm_index += 1
        room_assignments.append(room_assignment)

    skipflag = False

    # check for multiple rooms
    for code in room_assignments[0]:
        if code != 'None':
            if code in room_assignments[1] or code in room_assignments[2]:
                skipflag = True
    for code in room_assignments[1]:
        if code != 'None':
            if code in room_assignments[0] or code in room_assignments[2]:
                skipflag = True

    # skip if needed
    if skipflag:
        continue

    if room_assignments not in unique_assignments:
        unique_assignments.append(room_assignments)
        print room_assignments