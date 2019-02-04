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

print(str(result))

result2 = [(y for y in x) if isinstance(x, list) else x for x in [a, b, c]]

print(str(result2))