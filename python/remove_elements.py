'''
it's just a coincidence that this works. This won't work with %5 because
list items get shifted as items before them are deleted

'''

test = range(0, 30)
print("before:")
print(test)
print("")
for index, val in enumerate(test):
    print(index)
    if val % 2 == 0:
        del test[index]

print("\nafter:")
print test
print("")

# concise way:
test = range(0, 30)
print("before:")
print(test)
print("")
test = [num for num in test if num % 2 != 0]
print("\nafter:")
print test
print("")

# if you need try except:
test = range(0, 30)
test[0] = "Hello"
test[6] = "Howdy"
test[17] = "Yep"
print("before:")
print(test)
print("")
temp = []
for val in test:
    try:
        if val % 2 != 0:
            temp.append(val)
    except:
        continue
test = temp
print("\nafter:")
print test
print("")

