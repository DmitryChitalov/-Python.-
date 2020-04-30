"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
import random

array = [random.randint(0, 10) for i in range(20)]
print(array)

m = 0
num = 0
for i in array:
    count = array.count(i)
    if count > m:
        m = count
        num = i

print(f'Чаще всего встречается число {num}, оно появилось в массиве {m} раз(а)')

#Решение через ф-ю max:
new_array = []
for el in array:
    count2 = array.count(el)
    new_array.append(count2)

print(new_array)
max_2 = max(new_array)
elem = array[new_array.index(max_2)]
print(f'Чаще всего встречается число {elem}, оно появилось в массиве {max_2} раз(а)')