colors = [
    'red',
    'red-purple',
    'purple',
    'blue-purple',
    'blue',
    'blue-green',
    'green',
    'yellow-green',
    'yellow',
    'yellow-orange',
    'orange',
    'red-orange'
]

analogous_color_schemes = []
analogous_color_schemes_dict = {}

for num_colors in range(2,5):
    analogous_color_schemes_dict[num_colors] = []
    for i in range(0,len(colors)):
        try:
            analogous_color_scheme = []
            for j in range(i, i + num_colors):
                analogous_color_scheme.append(colors[j])
            analogous_color_schemes.append(analogous_color_scheme)
            analogous_color_schemes_dict[num_colors].append(analogous_color_scheme)
        except:
            continue

# for analogous_color_scheme in analogous_color_schemes:
#     print(analogous_color_scheme)

for group_size in analogous_color_schemes_dict:
    print("Size " + str(group_size) + ":\n")
    for analogous_color_scheme in analogous_color_schemes_dict[group_size]:
        out = "[ "
        for color in analogous_color_scheme:
            if color is not analogous_color_scheme[-1]:
                out += "%-14s "%(color+",")
            else:
                out += "%-13s"%(color)
        print(out + " ]")
    print("")

'''

# Verify that no groups have been repeated

import itertools

for analogous_color_scheme in analogous_color_schemes:
    rest = [x for x in analogous_color_schemes if x is not analogous_color_scheme]
    for y in rest:
        if analogous_color_scheme in itertools.permutations(y):
            print(y)
            print(analogous_color_scheme)
            print("")
'''     


        
'''
Output:

Size 2:

[ red,           red-purple    ]
[ red-purple,    purple        ]
[ purple,        blue-purple   ]
[ blue-purple,   blue          ]
[ blue,          blue-green    ]
[ blue-green,    green         ]
[ green,         yellow-green  ]
[ yellow-green,  yellow        ]
[ yellow,        yellow-orange ]
[ yellow-orange, orange        ]
[ orange,        red-orange    ]

Size 3:

[ red,           red-purple,    purple        ]
[ red-purple,    purple,        blue-purple   ]
[ purple,        blue-purple,   blue          ]
[ blue-purple,   blue,          blue-green    ]
[ blue,          blue-green,    green         ]
[ blue-green,    green,         yellow-green  ]
[ green,         yellow-green,  yellow        ]
[ yellow-green,  yellow,        yellow-orange ]
[ yellow,        yellow-orange, orange        ]
[ yellow-orange, orange,        red-orange    ]

Size 4:

[ red,           red-purple,    purple,        blue-purple   ]
[ red-purple,    purple,        blue-purple,   blue          ]
[ purple,        blue-purple,   blue,          blue-green    ]
[ blue-purple,   blue,          blue-green,    green         ]
[ blue,          blue-green,    green,         yellow-green  ]
[ blue-green,    green,         yellow-green,  yellow        ]
[ green,         yellow-green,  yellow,        yellow-orange ]
[ yellow-green,  yellow,        yellow-orange, orange        ]
[ yellow,        yellow-orange, orange,        red-orange    ]


'''