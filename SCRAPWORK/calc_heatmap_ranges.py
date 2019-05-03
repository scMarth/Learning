# MAXVALUE = 25921
MAXVALUE = 14653
num_bins = 50

factor = float(MAXVALUE)/num_bins

# numbers = [630, 1387, 2350, 3627, 5372, 7513, 10108, 13680, 18713, 25921]
numbers = [184, 409, 668, 976, 1368, 1882, 2570, 3390, 4784, 7218]
colors = ['#00FF00', '#39FF00', '#71FF00', '#AAFF00', '#E3FF00', '#FFE300', '#FFAA00', '#FF7100', '#FF3900', '#FF0000']

bounds = []
for number in numbers:
    bounds.append(number/factor)

boundaries = list(zip(bounds, colors))

for boundary in boundaries:
    print("'{}':'{}',".format(boundary[0], boundary[1]), end=" ")