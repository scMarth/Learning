# return the sorted hash 'input_hash', heys must be ints or strings
def sort_dict(input_hash):
    sorted_hash = {}
    
    # find out which keys are strings and which are numbers
    num_keys = [] # keys that are numbers
    str_keys = [] # keys that are strings
    for key in input_hash:
        if isinstance(key, str):
            str_keys.append(key)
        elif isinstance(key, int):
            num_keys.append(key)

    # put in the number keys first in sorted order
    for key in sorted(num_keys):
        sorted_hash[key] = input_hash[key]

    # put in the string keys next in sorted order
    for key in sorted(str_keys):
        sorted_hash[key] = input_hash[key]

    return sorted_hash

hashmap = {
   "A" : 120,
   "B" : 8,
   "C" : 87,
   "D" : 54,
   "E" : 45,
   2 : 20,
   1 : 58
}

print(sort_dict(hashmap))