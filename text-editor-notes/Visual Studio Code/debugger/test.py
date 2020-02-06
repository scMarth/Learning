def some_func():
    print('returning')

var_one = 1
var_two = 2

for i in range(10):
    var_one += 1
    var_two += 2
    if var_two == 4:
        some_func()

print('Done')