"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import timeit
import cProfile
import random

# user_list = [8, 3, 15, 6, 4, 2]
# second_list = []
# res_list = []
# # # Вариант 1
# for i in user_list:
#     if i % 2 == 0:
#         second_list.append(user_list.index(i))
# print(second_list)
# print(timeit.timeit('second_list = []', number=100000))
# cProfile.run('second_list')
# # # Вариант 2
# res = [res_list.append(user_list.index(i)) for i in user_list if i % 2 == 0]
# print(res_list)
# print(timeit.timeit('res_list = []', number=100000))
# cProfile.run('res_list')


# # # Вариант из урока
#
#
# def task_2(my_list):
#
#     print(
#         f'Исходный массив {my_list}, результат: '
#         f'{[el for el in range(len(my_list)) if my_list[el] % 2 == 0]}')
#
#
# MAIN_LIST = [3, 7, 12, 15, 8, 10, 4]
# task_2(MAIN_LIST)
# cProfile.run('task_2')

"""
def func(res_array):
    # print(f'Твой список: {res_array}')
    min_idx = 0
    max_idx = 0
    step = 1
    res = 0

    for i in res_array:
        if res_array[min_idx] > i:
            min_idx = res_array.index(i)
        elif res_array[max_idx] < 1:
            max_idx = res_array.index(i)

    if max_idx - min_idx < 0:
        step = -1

    for i in res_array[min_idx + step:max_idx:step]:
        res += i

    return (f'сумма элементов между минимальным элементом списка {res_array[min_idx]} \n'
            f'и максимальным {res_array[max_idx]} равна {res}')


USER_ARRAY = [randint(-100, 100) for i in range(15)]
func(USER_ARRAY)

cProfile.run('func')
print(timeit.timeit('func(USER_ARRAY)', number=10000, globals=globals()))

USER_ARRAY_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
func(USER_ARRAY_2)
print(timeit.timeit('func(USER_ARRAY_2)', number=10000, globals=globals()))

USER_ARRAY_3 = []
for i in range(-100, 100):
    if i <= 15:
        USER_ARRAY_3.append(i)
print(timeit.timeit('USER_ARRAY_3 = []', number=10000))
"""

# Еще вариант:


def func_max(size):
    array = [random.randint(size * -10 , size * 10) for _ in range(size)]

    i = 0
    index = -1

    while i < size:
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i
        i += 1
    if index != -1:
        return f'Максимальное отрициательное число {array[index]} ' \
               f'находится в ячейке {index}'


# c увеличением размера массива пропорционально возрастает скорость
# выполнения функции
print(timeit.timeit('func_max(10)' , number=100 , globals=globals()))
""""скорость выполнения 0.0028898869999999938 """
print(timeit.timeit('func_max(100)' , number=100 , globals=globals()))
""" скорость выполнения0.02322386800000001 """
print(timeit.timeit('func_max(1000)' , number=100 , globals=globals()))
""" скорость выполнения0.158008933 """

cProfile.run('func_max(10)')
cProfile.run('func_max(100)')
cProfile.run('func_max(1000)')
""""при формирование массива затрачивается время в зависимости от его размера, что явно видно при занчении 1000, 
если вынести генрацию массива за пределы функции, алгоритм будет быстрее.
"""

