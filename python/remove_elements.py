test = range(0, 30)
print("before:")
print(test)

for index, val in enumerate(test):
    if val % 2 == 0:
        del test[index]

print("\nafter:")
print test
