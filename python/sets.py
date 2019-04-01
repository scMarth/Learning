my_set = set()

# add stuff to the set
my_set.add(1)
my_set.add("one")

print(my_set)

# adding the same element again does nothing
my_set.add(1)
my_set.add(1)
my_set.add(1)
print(my_set)

# remove something
my_set.remove(1) # note, trying to remove 1 after this will cause an error
print(my_set)

# remove something if it is there
my_set.discard(1)
print(my_set)

# pop (no arguments to specify)
print(my_set.pop())
print(my_set)

# empty the set
for i in range(0, 11):
    my_set.add(i)
print(my_set)

# check if something is in the set
if 1 in my_set:
    print("1 is in the set")


# clear the set
my_set.clear()
print(my_set)