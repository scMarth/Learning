array = [0, "hello", "one", 3, (3, 4), "asdf", True, False]

print("Before:")
print(array)
print("")

new_array = [list(x) if isinstance(x, tuple) else x for x in array] # cast tuples to lists

print("After:")
print(new_array)
print("")


