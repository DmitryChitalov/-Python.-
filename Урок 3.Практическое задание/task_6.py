"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
"""
import random

r = [random.randint(0, 99) for _ in range(10)]
print(f'Массив: {r}')

min_index = 0
max_index = 0
step = 1
sum = 0

for i in r:
    if r[min_index] > i:
        min_index = r.index(i)
    elif r[max_index] < i:
        max_index = r.index(i)

if max_index - min_index < 0:
    step = -1

for i in r[min_index + step:max_index:step]:
    sum += i
    # print(f'DEBUG i={i}')

print(
        f'Сумма элементов между минимальным ({r[min_index]})',
        f' и максимальным ({r[max_index]}) элементами: {sum}'
        )