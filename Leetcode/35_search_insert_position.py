import math
        
def binary_search_call(arr, target):

    l = 0
    r = len(arr) - 1
    while l < r:
        mid = math.floor((l + r)/2)
        print("l: {} ; m: {} ; r: {}".format(l, mid, r))
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    if arr[l] < target:
        return l + 1
    else:
        return l





arr = range(0, 20)
target = 22
print(str(arr))

print("Target: {0}".format(target))
print("answer: " + str(binary_search_call(arr, target)))
print("")

target = 4
print("Target: {0}".format(target))
print("answer: " + str(binary_search_call(arr, target)))
print("")

target = -1
print("Target: {0}".format(target))
print("answer: " + str(binary_search_call(arr, target)))
print("")

target = 8
print("Target: {0}".format(target))
print("answer: " + str(binary_search_call(arr, target)))
print("")

target = 18
print("Target: {0}".format(target))
print("answer: " + str(binary_search_call(arr, target)))
print("")


target = 18.5
print("Target: {0}".format(target))
print("answer: " + str(binary_search_call(arr, target)))
print("")


target = 3.5
print("Target: {0}".format(target))
print("answer: " + str(binary_search_call(arr, target)))
print("")

arr = [1]
target = 1
print("Target: {0}".format(target))
print("answer: " + str(binary_search_call(arr, target)))
print("")

arr = [1, 3]
target = 4
print("Target: {0}".format(target))
print("answer: " + str(binary_search_call(arr, target)))
print("")

arr = [1, 3]
target = 0
print("Target: {0}".format(target))
print("answer: " + str(binary_search_call(arr, target)))
print("")

'''

Scrap:

binary saerch

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

[1, 3]
 0

l r m
0 1 0

'''