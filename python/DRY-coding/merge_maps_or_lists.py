def merge_string_arrays_redundant(array1, array2):
    result = []

    for string in array1:
        if string not in result:
            result.append(string)

    for string in array2:
        if string not in result:
            result.append(string)

    return result

def merge_string_arrays_dry(array1, array2):
    result = []
    for array in [array1, array2]:
        if array == []:
            continue
        for string in array:
            if string not in result:
                result.append(string)
    return result

def merge_str_to_arr_map_redundant(map1, map2):
    result = {}

    for key in map1:
        if key not in result:
            result[key] = []
        array = map1[key]

        for string in array:
            if string not in result[key]:
                result[key].append(string)

    for key in map2:
        if key not in result:
            result[key] = []
        array = map2[key]

        for string in array:
            if string not in result[key]:
                result[key].append(string)

    return result

def merge_str_to_arr_map_dry(map1, map2):
    result = {}
    for hashmap in [map1, map2]:
        if hashmap == {}:
            continue
        for key in hashmap:
            if key not in result:
                result[key] = []
            for string in hashmap[key]:
                if string not in result[key]:
                    result[key].append(string)
    return result

def dump_str_to_arr_hash(hashmap):
    for key in hashmap:
        print("\t" + key)
        for string in hashmap[key]:
            print("\t\t" + string)

array1 = range(1,10)
array2 = range(8,17)

str_to_arr_map1 = {
    "key1" : [
        "path1",
        "path2",
        "path3"
    ],
    "key2" : [
        "path4",
        "path5",
        "path6",
        "path7"
    ]
}

str_to_arr_map2 = {
    "key2" : [
        "path5",
        "path6",
        "path7",
        "path8",
        "path9"
    ],
    "key3" : [
        "path10"
    ]
}

print("===============================================================")
print("str_to_arr_map1:")
dump_str_to_arr_hash(str_to_arr_map1)
print("str_to_arr_map2:")
dump_str_to_arr_hash(str_to_arr_map2)
print("result:")
dump_str_to_arr_hash(merge_str_to_arr_map_redundant(str_to_arr_map1, str_to_arr_map2))
print("str_to_arr_map1:")
dump_str_to_arr_hash(str_to_arr_map1)
print("str_to_arr_map2:")
dump_str_to_arr_hash(str_to_arr_map2)

print("===============================================================")
print("str_to_arr_map1:")
dump_str_to_arr_hash(str_to_arr_map1)
print("str_to_arr_map2:")
dump_str_to_arr_hash(str_to_arr_map2)
print("result:")
dump_str_to_arr_hash(merge_str_to_arr_map_dry(str_to_arr_map1, str_to_arr_map2))
print("str_to_arr_map1:")
dump_str_to_arr_hash(str_to_arr_map1)
print("str_to_arr_map2:")
dump_str_to_arr_hash(str_to_arr_map2)

print("===============================================================")
print(merge_string_arrays_redundant(array1, array2))
print("")

print("===============================================================")
print(merge_string_arrays_dry(array1, array2))
print("")
