import heapq

# min heaps in python

arr = [1, 34, 2, 12, 56, 86, 34, 2, 1]
print(arr)

heapq.heapify(arr)
print(arr)

print(heapq.heappop(arr))
print(arr)

print(heapq.heappop(arr))
print(arr)

print(heapq.heappop(arr))
print(arr)

while arr:
    print(heapq.heappop(arr))
    print(arr)

print("")
heapq.heappush(arr, 34)
print(arr)
heapq.heappush(arr, 3)
print(arr)
heapq.heappush(arr, 3)
print(arr)
heapq.heappush(arr, 6)
print(arr)
heapq.heappush(arr, 3)
print(arr)
heapq.heappush(arr, 2)
print(arr)
heapq.heappush(arr, 87)
print(arr)
print("")


#max heap
arr2 = [1, 34, 2, 12, 56, 86, 34, 2, 1]
heapq._heapify_max(arr2)
while arr2:
    print(heapq._heappop_max(arr2))
    print(arr2)
    print("")