"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
import random
import statistics

m = int(input("Введите число m: "))
n = 2 * m + 1
array = [random.randint(0, 10) for i in range(n)]
print(array)


def median(arr):
    k = 0
    while k < n:
        arr_part_1 = []
        arr_part_2 = []
        for i in range(n):
            if arr[i] < arr[k]:
                arr_part_1.append(arr[i])
            elif arr[i] == arr[k] and k > i:
                arr_part_1.append(arr[i])
            elif arr[i] == arr[k] and k < i:
                arr_part_2.append(arr[i])
            elif arr[i] > arr[k]:
                arr_part_2.append(arr[i])
        if len(arr_part_1) == len(arr_part_2):
            return arr[k]
        k += 1


print(f'Медиана списка: {median(array)}')

print(f'Медиана списка (модуль статистика): {statistics.median(array)}')

""" 
Получилось сделать нахождение медианы без сортировки: просто раскладываем на два массива числа больше и меньше данного, 
а потом сравниваем по длине. Похожий вариант потои увидела в решении №1 при разборе ДЗ. Добавила модуль статистики для
проверки и переделала код - не всегда корректно срабатывало, есил число-медиана повторяется в списке.

"""
