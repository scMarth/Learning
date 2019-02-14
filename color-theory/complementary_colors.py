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

for i in range(6, len(colors)):
    # print('{0} & {1}'.format())
    print('[ %-14s %-13s ]'%(colors[i-6] + ",", colors[i]))

'''

Output

[ red,           green         ]
[ red-purple,    yellow-green  ]
[ purple,        yellow        ]
[ blue-purple,   yellow-orange ]
[ blue,          orange        ]
[ blue-green,    red-orange    ]

'''