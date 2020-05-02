"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
from random import random

N = int(input("Введите длину массива: "))
my_arr = [int(random()*10) for i in range(N)]
print(my_arr)
max_arr = max(my_arr, key=my_arr.count)
print(f"Число {max_arr} встречается чаще всего: {my_arr.count(max_arr)} раз")