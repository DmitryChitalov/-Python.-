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

# initial = [8, 3, 15, 6, 4, 2]
# final = []
# x = [num for num in range(len(initial) + 1) if num % 2 == 0]
# print(x)

# y = list(filter(lambda num: num % 2 == 0, initial)) # using lambda function - how to get even numbers
# print(y)


# В этой задаче есть вопросы:
# 1. насколько оправдано использование index  в решении с циклами?
# как при помощи lambda фунцкии сделать такое решение? Пробовал сам, но не получилось - при использовании if else выдает ошибки


#  Solution from teacher
def task_2_1(origin_lst):
    new_lst = []
    for elem in origin_lst:
        if elem % 2 == 0:
            new_lst.append(origin_lst.index(elem))
    print(f"Исходный массив: {origin_lst}, результат: {new_lst}")


def task_2_2(origin_lst):
    print(f"Исходный массив: {origin_lst}")
    print(f"{[elem for elem in range(len(origin_lst)) if origin_lst[elem] % 2 == 0]}")


ORIGIN_LIST = [8, 3, 15, 6, 4, 2]
task_2_1(ORIGIN_LIST)
task_2_2(ORIGIN_LIST)
