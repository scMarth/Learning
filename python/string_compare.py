import math

pairs = [
    ['Hello', 'Hello'],
    ['Hello', None],
    [None, 'Hello'],
    [None, None],
    ['Hello', 'hi'],
    ['Hel'+'lo', 'hi']
]

for pair in pairs:
    strA, strB = pair
    print("{} ; {}".format(strA, strB))

    # enters if statement if false
    if strA != strB:
        print("Signal 1")

    # works
    if not strA == strB:
        print("Signal 2")

    if not (strA == strB):
        print("Signal 3")

    if (not strA) == strB:
        print("Signal 4")

    print("")