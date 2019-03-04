# a not useful workspace for reverse-engineering lighten() and darken() in sass

normal = {
    'name' : 'Normal',
    'red' : 201,
    'green' : 203,
    'blue' : 207
}

darkened_30p = {
    'name' : 'Darkened 30%',
    'red' : 120,
    'green' : 125,
    'blue' : 135    
}

darkened_15p = {
    'name' : 'Darkened 15%',
    'red' : 161,
    'green' : 164,
    'blue' : 171
}

lightened_15p = {
    'name' : 'Lightened 15%',
    'red' : 242,
    'green' : 242,
    'blue' : 243
}

lightened_30p = {
    'name' : 'Lightened 30%',
    'red' : 255,
    'green' : 255,
    'blue' : 255
}

print("Deltas:\n")
for new_color in [darkened_30p, darkened_15p, normal, lightened_15p, lightened_30p]:
    print("rgb(%3d, %3d, %3d) ; %s"%(new_color['red'], new_color['green'], new_color['blue'], new_color['name']))
    for color in ['red', 'green', 'blue']:
        delta = normal[color] - new_color[color]
        print("\t{} delta: {}".format(color, delta))
    print("")
