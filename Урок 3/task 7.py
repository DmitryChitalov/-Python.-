from random import random
size = 10
arr = list(range(0,size))
for i in range(size):
    arr[i] = int(random()*100)

def min_id(arr):
    min = arr[0]
    min_id = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_id = i
    return min_id

print(arr)
print(arr[min_id(arr)])
arr.remove(arr[min_id(arr)])
print(arr[min_id(arr)])