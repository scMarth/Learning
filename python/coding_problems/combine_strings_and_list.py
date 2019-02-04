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