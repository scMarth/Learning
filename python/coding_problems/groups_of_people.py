# https://stackoverflow.com/questions/54369870/python-combination-without-repetition-with-sublists-items
# incomplete

import itertools, sys

people = ['A', 'A', 'B', 'B', 'C']
rooms = [2, 3, 2]

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
    if person_code not in codes:
        codes.append(person_code)
print codes

# get combinations of codes
for perm in itertools.permutations(codes):
    fits = True
    perm_index = 0
    room_index = 0

    room_arrangement = []

    curr_group = []
    room_size = rooms[room_index]

    while True:
        if perm_index >= len(perm):
            break

        if code_count[perm[perm_index]] < room_size:
            # print("case 1")
            for i in range(0, code_count[perm[perm_index]]):
                curr_group.append(perm[perm_index])
                room_size -= 1
            perm_index += 1
        elif code_count[perm[perm_index]] == room_size:
            # print("case 2")
            for i in range(0, room_size):
                curr_group.append(perm[perm_index])
            room_arrangement.append(curr_group)
            curr_group = []
            perm_index += 1
            room_index += 1

            if room_index >= len(rooms):
                if perm_index >= len(perm):
                    fits = False
                break

            room_size = rooms[room_index]
        else: # code_count[perm[perm_index]] > room_size:
            # print("case 3")
            for i in range(0, room_size):
                curr_group.append(None)
            room_arrangement.append(curr_group)
            curr_group = []
            room_index += 1

            if room_index >= len(rooms):
                if perm_index >= len(perm):
                    fits = False
                break

            room_size = rooms[room_index]

    print perm
    if fits:
        print room_arrangement
    print("")