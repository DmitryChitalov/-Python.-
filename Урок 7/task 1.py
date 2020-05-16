from random import randint
from datetime import datetime


N = 10000
arr = []
for i in range(N):
    arr.append(randint(0, 50))
print(arr)


def func(arr):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


start_time = datetime.now()
arr = func(arr)
print(arr)
print(f"Время: {datetime.now() - start_time}")
