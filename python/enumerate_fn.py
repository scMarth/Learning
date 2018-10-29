'''

The optional argument allows us to tell enumerate from where to start the index. You can also create tuples containing the index and list item using a list.

http://book.pythontips.com/en/latest/enumerate.html

(22, 'apple')
(23, 'banana')
(24, 'grapes')
(25, 'pear')

(0, 'apple')
(1, 'banana')
(2, 'grapes')
(3, 'pear')

'''

my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 22):
    print(c, value)

# without the optional argument:
print("")
for c, value in enumerate(my_list):
    print(c, value)