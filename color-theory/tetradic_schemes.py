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
    split_hue1 = (i + 1)%12
    split_hue2 = (i + 11)%12

    split_complement1 = (i + 5)%12
    split_complement2 = (i + 7)%12

    print('[ %-14s %-14s %-14s %-13s ]'%(
        colors[split_hue1] + ",",
        colors[split_hue2] + ",",
        colors[split_complement1] + ",",
        colors[split_complement2]
    ))

'''

[ red-purple,    red-orange,    blue-green,    yellow-green  ]
[ purple,        red,           green,         yellow        ]
[ blue-purple,   red-purple,    yellow-green,  yellow-orange ]
[ blue,          purple,        yellow,        orange        ]
[ blue-green,    blue-purple,   yellow-orange, red-orange    ]
[ green,         blue,          orange,        red           ]
[ yellow-green,  blue-green,    red-orange,    red-purple    ]
[ yellow,        green,         red,           purple        ]
[ yellow-orange, yellow-green,  red-purple,    blue-purple   ]
[ orange,        yellow,        purple,        blue          ]
[ red-orange,    yellow-orange, blue-purple,   blue-green    ]
[ red,           orange,        blue,          green         ]

'''