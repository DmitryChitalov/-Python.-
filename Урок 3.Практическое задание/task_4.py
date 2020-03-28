"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
import random

arr = [random.randint(0, 20) for i in range(30)]
arr.sort()
print(arr)
print(max(arr, key=arr.count))
