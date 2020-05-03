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

# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).


import timeit


# Вариант 1 - цикл
def get_even_odd_1_cycle(number):
    number_even, number_odd = 0, 0  # Счетчики четных и нечетных цифр
    number_i = number  # Число для использования в итерациях (будет изменяться)
    while True:
        if number_i % 10 % 2:
            number_odd += 1
        else:
            number_even += 1
        number_i = number_i // 10
        if not number_i:
            break
    return number_even, number_odd


# Вариант 2 - рекурсия
def get_even_odd_2_recursion(number):
    # условие завершения рекурсии
    if not number:
        return 0, 0
    # условие рекурсивного вызова
    number_even, number_odd = get_even_odd_2_recursion(number // 10)
    if number % 10 % 2:
        number_odd += 1
    else:
        number_even += 1
    return number_even, number_odd


# Вариант 3 - цикл - оптимизировано
def get_even_odd_3_cycle(number):
    number_even, number_odd = 0, 0  # Счетчики четных и нечетных цифр
    for c in str(number):
        if c in ('1', '3', '5', '7', '9'):
            number_odd += 1
        else:
            number_even += 1
    return number_even, number_odd


# Вариант 4 - рекурсия - оптимизировано
def get_even_odd_4_recursion(number):
    # условие завершения рекурсии
    if not number:
        return 0, 0
    # условие рекурсивного вызова
    number_even, number_odd = get_even_odd_4_recursion(str(number)[:-1])
    if str(number)[-1] in ('1', '3', '5', '7', '9'):
        number_odd += 1
    else:
        number_even += 1
    return number_even, number_odd


# Вариант 5 - рекурсия - оптимизировано еще раз
def get_even_odd_5_recursion(number):
    # условие завершения рекурсии
    if not number:
        return 0, 0
    # условие рекурсивного вызова
    if isinstance(number, str):
        str_number = number
    else:
        str_number = str(number)
    number_even, number_odd = get_even_odd_4_recursion(str_number[:-1])
    if str_number[-1] in ('1', '3', '5', '7', '9'):
        number_odd += 1
    else:
        number_even += 1
    return number_even, number_odd


number_for_test = 987654321987654321987654321987654321
print(get_even_odd_1_cycle(number_for_test))
print(get_even_odd_2_recursion(number_for_test))
print(get_even_odd_3_cycle(number_for_test))
print(get_even_odd_4_recursion(number_for_test))
print(get_even_odd_5_recursion(number_for_test))

print("get_even_odd_1_cycle()    =",
      timeit.timeit("get_even_odd_1_cycle(987654321987654321987654321987654321)",
                    setup="from __main__ import get_even_odd_1_cycle",
                    number=1000))
print("get_even_odd_2_recursion()=",
      timeit.timeit("get_even_odd_2_recursion(987654321987654321987654321987654321)",
                    setup="from __main__ import get_even_odd_2_recursion",
                    number=1000))
print("get_even_odd_3_cycle()    =",
      timeit.timeit("get_even_odd_3_cycle(987654321987654321987654321987654321)",
                    setup="from __main__ import get_even_odd_3_cycle",
                    number=1000))
print("get_even_odd_4_recursion()=",
      timeit.timeit("get_even_odd_4_recursion(987654321987654321987654321987654321)",
                    setup="from __main__ import get_even_odd_4_recursion",
                    number=1000))
print("get_even_odd_5_recursion()=",
      timeit.timeit("get_even_odd_5_recursion(987654321987654321987654321987654321)",
                    setup="from __main__ import get_even_odd_5_recursion",
                    number=1000))


# Решил задачу с использованием цикла и рекурсии
# Затем каждую функцию попытался оптимизировать, преобразовав число в строку и работая с ней как с массивом
# Делаю анализ:
# get_even_odd_1_cycle()    = 0.015200099999999998
# get_even_odd_2_recursion()= 0.0255743
# get_even_odd_3_cycle()    = 0.008668200000000001
# get_even_odd_4_recursion()= 0.041118299999999997

# Циклы работают быстрее, чем рекурсии, это ожидаемо,
# так как в общем случае сложность цикла меньше чем сложность рекурсии из-за использования рекурсией стека вызовов
# При оптимизации цикла есть значительный эффект,
# так как уменьшаем количество математических операций с большими числами, преобразовав число в строку лишь однажды
# При оптимизации рекурсии эффект обратный,
# так как преобразование числа в строку происходит при каждом рекурсивном вызове
# На основании анализа решил еще раз оптимизировать рекурсию, исключив повторные преобрахования типов
# Делаю анализ:

# get_even_odd_1_cycle()    = 0.018241599999999997
# get_even_odd_2_recursion()= 0.026952899999999995
# get_even_odd_3_cycle()    = 0.00855460000000001
# get_even_odd_4_recursion()= 0.0411112
# get_even_odd_5_recursion()= 0.04128209999999999

# эффекта от дополнительной оптимизации не получил
# видимо функция isinstance(), вызваемая при каждом рекурсивном методе тоже достаточно затратная

# Вывод:
# из пяти проанализированных алгоритмов самым оптимальным в данном случае является
# get_even_odd_3_cycle - цикл с минимизацией математических операций с большими числами
