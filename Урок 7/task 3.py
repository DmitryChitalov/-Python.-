from random import randint
from datetime import datetime

N = 1000
arr = []
for i in range(N):
    arr.append(randint(0, 1234))
print(arr)

def func(arr):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = func(arr)

mid = int((len(arr)/2))
print(arr[mid])