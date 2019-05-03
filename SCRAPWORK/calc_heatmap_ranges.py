MAXVALUE = 14653
num_bins = 50

factor = float(MAXVALUE)/num_bins

numbers = [0, 185, 410, 669, 977, 1369, 1883, 2571, 3391, 4785]
colors = ['#00FF00', '#39FF00', '#71FF00', '#AAFF00', '#E3FF00', '#FFE300', '#FFAA00', '#FF7100', '#FF3900', '#FF0000']


bounds = []
for number in numbers:
    bounds.append(number/factor)

boundaries = list(zip(bounds, colors))

for boundary in boundaries:
    print("'{}':'{}',".format(boundary[0], boundary[1]), end=" ")