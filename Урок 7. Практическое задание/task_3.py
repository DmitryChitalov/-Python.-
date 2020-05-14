"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
import random

m = int(input("Введите число m: "))
n = 2 * m + 1
array = [random.randint(0, 10) for i in range(n)]
print(array)


def median(arr):
    k = 0
    while k < n:
        arr_part_1 = []
        arr_part_2 = []
        for i in arr:
            if i > arr[k]:
                arr_part_2.append(i)
            else:
                arr_part_1.append(i)
        if len(arr_part_1) == (len(arr_part_2) + 1):
            return arr[k]
        k += 1
    return


print(f'Медиана списка: {median(array)}')
