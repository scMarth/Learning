# https://stackoverflow.com/questions/54525409/combine-strings-and-list-of-strings-to-one-big-list

a = 'apples'
b = 'pears'
c = ['grapes', 'bananas', 'kiwis']

result = []
for obj in [a, b, c]:
    if isinstance(obj, list):
        result += obj
    else:
        result += [obj]

print result