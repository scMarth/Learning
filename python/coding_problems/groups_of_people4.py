peoples = ['A','A','B','B','C', "None", "None"]

import itertools

for x in itertools.permutations(peoples):
    rooma = x[:2]
    if rooma[0] == rooma[1] or "None" in rooma[:2]:
        roomb = x[2:5]
        if len(roomb) != len(set(roomb)):
            roomc = x[5:]
            if roomc[0] == roomc[1] or "None" in roomc[:2]:
                print([rooma,roomb,roomc])