# return the sorted hash 'input_hash'
def sort_dict(input_hash):
    sorted_hash = {}
    for key in sorted(input_hash):
        sorted_hash[key] = input_hash[key]
    return sorted_hash

test = {
    'asdfadsf' : 1,
    'xczv' : 1,
    'cvxv' : 1,
    'bbbb' : 1,
    'asdf' : 1
}

print(test)
test = sort_dict(test)
print(test)