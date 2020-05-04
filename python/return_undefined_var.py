# looks Python doesn't execute or check after the return statement

def some_function(num):
    num_range = range(num)
    return sum(num_range)
    return features
    features = features + 1

print(some_function(10))
# features = features + 1 # name 'features' is not defined