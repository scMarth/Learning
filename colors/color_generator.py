# generate 'num_colors_to_generate' amount of colors that are
# equidistant from the color spectrum

import itertools, sys, math

def color_string(red, green, blue):
    print("rgb({}, {}, {})".format(red, green, blue))

num_colors_to_generate = 10

codes = ['r', 'g', 'b']
range_map = {}

num = 0

for i in range(1, 4):
    for combination in itertools.combinations(codes, i):
        key = ""
        val = []
        for item in combination:
            key += str(item)
            ranges = []
            ranges.append(num)
            num += 255
            ranges.append(num)
            num += 1
            val.append(ranges)
        range_map[key] = val
        print("")
print(range_map)

