"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
import random

LST = [random.randint(-100, 100) for i in range(0,15)]

i = 0
print(LST)
while i < (len(LST) / 2):
    LST.remove(min(LST))
    i += 1
print(f'медиана: {min(LST)}')
