"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
# list_dig = [1, 2, 2, 1, 3, 1, 5, 6, 5, 6, 6, 2]
#
#
# def most_frequent(list_dig) -> str:
#     counter = {}
#     max = 1
#     number = None
#     for x in list_dig:
#         if x in counter:
#             counter[x] += 1
#         else:
#             counter[x] = 1
#         if counter[x] > max:
#             max = counter[x]
#             number = x
#     if number is not None:
#         return f"The number {number} is presented {max} times"
#     else:
#         print("All elements are unique")
#
#
# print(most_frequent(list_dig))

# В этой задаче есть вопрос:
# Если несколько числе встречаютс яодинаковое количество раз, то как их все вывести?
# Выводится первое число, которое встречается чаще всего. Вданном случае число 1

#  Solution from teacher

import random


def task_4(lst):
    print(f"Исходный массив: {lst}")

    numb = max(lst, key=lst.count)
    # print(numb)
    print(f"Число {numb} встречается {lst.count(numb)} раза")


LST = [random.randint(-100, 100) for i in range(50)]
task_4(LST)
