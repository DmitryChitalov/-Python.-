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

array = [random.randint(0, 100) for i in range(10)]
print(array)

a = min(array)
b = max(array)
a_ind = array.index(a) #7
b_ind = array.index(b) #3

if a_ind < b_ind:
    new_array = [el for el in array if (array.index(el) > a_ind and array.index(el) < b_ind)]
else:
    new_array = [el for el in array if (array.index(el) < a_ind and array.index(el) > b_ind)]

print(new_array)
sum_arr = sum(new_array)
print(f"Минимальное число массива {a}, максимальное число - {b}, сумма элементов между ними: {sum_arr}")