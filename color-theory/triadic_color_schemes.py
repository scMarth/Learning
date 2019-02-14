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

for i in range(0, len(colors)):
    try:
        print('[ %-14s %-14s %-13s ]'%(colors[i] + ",", colors[i+4] + ",", colors[i+8]))
    except:
        continue

'''

Output:

[ red,           blue,          yellow        ]
[ red-purple,    blue-green,    yellow-orange ]
[ purple,        green,         orange        ]
[ blue-purple,   yellow-green,  red-orange    ]

'''