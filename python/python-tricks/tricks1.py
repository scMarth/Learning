# ----------------------------------------------------------------------

cities = ['Marseille', 'Amsterdam', 'New York', 'London']

# The  bad way
i = 0
for city in cities:
    print(i, city)
    i += 1

print("")

# The good way
for i, city in enumerate(cities):
    print(i, city)

print("")

# ----------------------------------------------------------------------

x_list = [1,2,3]
y_list = [2,4,6]

# The bad way
for i in range(len(x_list)):
    x = x_list[i]
    y = y_list[i]
    print(x,y)

print("")

# The good way
for x, y in zip(x_list, y_list):
    print(x,y)

print("")

# ----------------------------------------------------------------------

x = 10
y = -10

print('Before: x = %d, y = %d' % (x, y))

# The bad way
tmp = y
y = x
x = tmp
print('After: x = %d, y = %d' % (x, y))

# The good way
x, y = y, x
print('After: x = %d, y = %d' % (x, y))

print("")

# ----------------------------------------------------------------------

ages = {
    'Mary'     : 31,
    'Jonathan' : 28,
    'Dick'     : 51
}

# The bad way
if 'Dick' in ages:
    age = ages['Dick']
else:
    age = 'Unknown'
print('Dick is %s years old' % age)

print("")

# The good way
age = ages.get('Dick', 'Unknown')
print('Dick is %s years old' % age)


print("")
# ----------------------------------------------------------------------

needle = 'd'
haystack = ['a', 'b', 'c']

# The bad way
found = False
for letter in haystack:
    if needle == letter:
        print("Found!")
        found = True
        break
if not found:
    print('Not found!')

print("")

# The good way
for letter in haystack:
    if needle == letter:
        print("Found!")
        break
else: # If no break occurred
    print('Not found!')

'''

Notes: else statement after a for-loop only executes if the for loop
completed every loop

'''

print("")

# The pYth0n1c way
print("Found!" if needle in haystack else "Not found!")

print("")

# The pYth0n1c way #2
found = needle in haystack
print(['Not found!', 'Found!'][found])

print("")

# The pYth0n1c way (super big brain)
print(['Not found!', 'Found!'][needle in haystack])


print("")
# ----------------------------------------------------------------------

# The bad way
f = open('pimpin-aint-easy.txt')
text = f.read()
for line in text.split('\n'):
    print(line)
f.close()

print("")

# The better way
f = open('pimpin-aint-easy.txt')
for line in f:
    print(line)
f.close()

print("")

# The good way
with open('pimpin-aint-easy.txt') as f:
    for line in f:
        print(line)

print("")
# ----------------------------------------------------------------------

print('Converting!')
print(int('1'))
print('Done!')

print("")

# with try-catch

print('Converting!')
try:
    print(int('x'))
except:
    print('Conversion failed!')
print('Done!')

print("")

# with else / finally

print('Converting!')
try:
    print(int('x'))
except:
    print('Conversion failed!')
else: # basically the opposite of except (if no-except)
    print('Conversion successful!')
finally: # always executed (still executed if exception occurs)
    print('Done!')

print("")