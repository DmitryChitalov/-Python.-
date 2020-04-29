from random import random

size = 20
arr = list(range(0, size))
for i in range(size):
    arr[i] = int(random()*10)

arr_count = list(range(0, size))

for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count+=1
    arr_count[i] = count
print("сами числа")
print(arr)
print("Количество раз")
print(arr_count)

def max_id(arr):
    max = arr[0]
    max_id = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
            max_id = i
    return max_id

print(f"Число {arr[max_id(arr_count)]} встречается больше всего раз")