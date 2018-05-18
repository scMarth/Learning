# double and single quotes exactly the same in python

print("Hello")
print('Hello')

'''
This is a multi-line
comment
in python
'''

variable = 'Derek'
print(variable)

# variable must start with letter, and then it can have numbers or underscores

# 5 main data types: numbers, strings, lists, tuples, dictionaries

# math operations:

# + - *
# / % 
# ** (exponential)
# // (floor division)

print(2**8)
print(9//2)

print("1 + 2 - 3 * 2 = ", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2 = ", (1 + 2 - 3) * 2)


quote = "\" <-- quote"

multi_line_quote = ''' The quick
brown fox'''

print(multi_line_quote)

print("%s %s %s" % ('I like the quote', quote, multi_line_quote))

# print("I don't like the new line", end="") # only works in python 3+

print('\n' * 5)

stringVar = "Hello " * 5
print(stringVar)

grocery_list = [
   'Juice',
   'Tomatoes',
   'Potatoes',
   'Bananas'
]

print(grocery_list[1:4]) # last index isn't included

grocery_list.append('Peanuts')
grocery_list.insert(1, "Pickles")

print(grocery_list)

grocery_list.remove("Pickles")

grocery_list.sort()

grocery_list.reverse()

del grocery_list[0]

print(grocery_list)

grocery_list = grocery_list + grocery_list

print(grocery_list)

print(len(grocery_list))
print(min(grocery_list)) # alphabetically
print(max(grocery_list)) # alphabetically

pi_tuple = (3, 1, 4, 1, 5, 9)

new_tuple = list(pi_tuple)
new_tuple = tuple(new_tuple)

print(len(new_tuple))
print(min(new_tuple))
print(max(new_tuple))

hashMap = {
   1 : "one",
   2 : "two",
   3 : "three"
}

print(hashMap)

del hashMap[2]

print(hashMap)

print(hashMap.keys())
print(hashMap.values())


class Animal:
   __name = "" # double underscore means that this variable is private to this class



