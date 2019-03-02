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

for i in range(0, 3):

    print('[ %-14s %-14s %-14s %-13s ]'%(
        colors[i % 12] + ",",
        colors[(i + 3) % 12] + ",",
        colors[(i + 6) % 12] + ",",
        colors[(i + 9) % 12]
    ))

'''

Output:

[ red,           blue-purple,   green,         yellow-orange ]
[ red-purple,    blue,          yellow-green,  orange        ]
[ purple,        blue-green,    yellow,        red-orange    ]

'''