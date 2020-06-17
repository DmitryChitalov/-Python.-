"""
Задание_2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.

Подсказка:
Попробуйте решить эту задачу в одну строку (такое решение точно есть)

Пример:
Исходный массив: [8, 3, 15, 6, 4, 2], результат: [0, 3, 4, 5]
"""

#  Solution with cycle
# for num in initial:
#     if num % 2 == 0:
#         final.append(initial.index(num))
#     else:
#         continue
# print(final)

initial = [8, 3, 15, 6, 4, 2]
final = []
x = [num for num in range(len(initial) + 1) if num % 2 == 0]
print(x)

# y = list(filter(lambda num: num % 2 == 0, initial)) # using lambda function how to get even numbers
# print(y)






