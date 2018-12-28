array = [
    3742,
    (5782365.6267064, 2139701.6357287397),
    270,
    u'R_118_2T',
    0.05979062616825104,
    0.002989531261846423,
    u'R',
    119,
    33,
    u'W',
    u'GABILAN',
    u'ST',
    u'',
    u'DS',
    0,
    0,
    0,
    1854656824.0,
    927328412.0,
    238,
    u'Tuesday',
    u'Second Tuesday',
    315.6322931699773,
    u'W GABILAN ST'
]

print(array)
print("")

converted_array = []
last_value_index = len(array) - 1
for value in array[0:last_value_index]:
    if isinstance(value, unicode):
        converted_array.append(str(value))
    else:
        converted_array.append(value)
print(converted_array)
print("")

shorthand_converted_array = [str(value) if isinstance(value, unicode) else value for value in array[0:last_value_index]]
print(shorthand_converted_array)
