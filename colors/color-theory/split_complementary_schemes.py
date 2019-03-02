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
    split_complement1 = (i + 5)%12
    split_complement2 = (i + 7)%12

    print('[ %-14s %-14s %-13s ]'%(
        colors[i] + ",",
        colors[split_complement1] + ",",
        colors[split_complement2]
    ))

'''

Output:

[ red,           blue-green,    yellow-green  ]
[ red-purple,    green,         yellow        ]
[ purple,        yellow-green,  yellow-orange ]
[ blue-purple,   yellow,        orange        ]
[ blue,          yellow-orange, red-orange    ]
[ blue-green,    orange,        red           ]
[ green,         red-orange,    red-purple    ]
[ yellow-green,  red,           purple        ]
[ yellow,        red-purple,    blue-purple   ]
[ yellow-orange, purple,        blue          ]
[ orange,        blue-purple,   blue-green    ]
[ red-orange,    blue,          green         ]

'''