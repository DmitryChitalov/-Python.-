from random import random
x = int(input("Количество строк: "))
y = int(input("Количество столбцов: "))

arr = []
for r in range(x):
    arr.append([])
    for c in range(y):
        arr[r].append(int(random()*10))

def sum(arr):
    num = 0
    for i in arr:
        num+=i
    return num

def max_id(arr):
    max = arr[0]
    max_id = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
            max_id = i
    return max_id

def min_id(arr):
    min = arr[0]
    min_id = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_id = i
    return min_id

arr_sum = []
for i in arr:
    arr_sum.append(sum(i))

print(arr)
min = min_id(arr_sum)
print(arr[min_id(arr_sum)])
max = max_id(arr[min_id(arr_sum)])
print(arr[min][max])
