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

import random
import timeit

""" Задача 1 """
"""
Функция формирования из введенного числа обратное по порядку входящих в него
цифр. Например, если введено число 3486, то в результате функция выводит число 6843.
"""


def func_revers_number(number):
    """
    Функция формирования из введенного числа обратное по порядку входящих в него
    цифр. Например, если введено число 3486, то в результате функция выводит число 6843.

    :param number: число, которое ввел пользователь
    :return: число, сформированное из введенного числа
    с обратным порядком входящих в исходное число цифр
    """
    inverse_number = 0
    # Цикл выполняется пока поочередно перебирая цифры числа не дойдет до последней цифры
    while number > 0:
        # находим последнюю цифру числа
        # увеличиваем разрядность второго числа
        # добавляем очередную цифру к формируемому перевернутому числу
        inverse_number = inverse_number * 10 + number % 10
        # переходим к следующей цифре исходного числа
        number //= 10
    return inverse_number


# Рекурсивная функция формирования из введенного числа обратное по порядку входящих в него
# цифр. Например, если введено число 3486, то в результате функция выводит число 6843.
def rec_reverse_number(number, inverse_number=0):
    """
    Рекурсивная функция формирования из введенного числа обратное по порядку входящих в него
    цифр. Например, если введено число 3486, то в результате функция выводит число 6843.

    :param number: число, которое ввел пользователь
    :param inverse_number:
    :return: число, сформированное из введенного числа
    с обратным порядком входящих в исходное число цифр
    """
    if number == 0:
        return inverse_number
    # Цикл выполняется пока поочередно перебирая цифры числа не дойдет до последней цифры
    else:
        # увеличиваем разрядность второго числа
        # добавляем очередную цифру к формируемому перевернутому числу
        inverse_number = inverse_number * 10 + number % 10
        # переходим к следующей цифре исходного числа
        return rec_reverse_number(number // 10, inverse_number)


# Функция мемоизации для рекурсивной функции "rec_reverse_number"
# как способ оптимизации, при котором сохраняется результат выполнения функции
# и этот результат используется при следующем вызове
def memoization(function):
    """
    Функция мемоизации для рекурсивной функции "rec_reverse_number"
    как способ оптимизации, при котором сохраняется результат выполнения функции
    и этот результат используется при следующем вызове

    :param function: рекурсивная функция
    :return: сохраненный результат
    """

    def wrapper(n, memory={}):
        value = memory.get(n)
        if value is None:
            value = function(n)
            memory[n] = value
        return value

    return wrapper


@memoization
def mem_reverse_number(number, inverse_number=0):
    if number == 0:
        return inverse_number
    # Цикл выполняется пока поочередно перебирая цифры числа не дойдет до последней цифры
    else:
        # увеличиваем разрядность второго числа
        # добавляем очередную цифру к формируемому перевернутому числу
        inverse_number = inverse_number * 10 + number % 10
        # переходим к следующей цифре исходного числа
        return rec_reverse_number(number // 10, inverse_number)


NUMBER = int(random.random() * pow(22, 20))
print(f'*********************************** Задача 1 ***********************************'
      f'\nФормирование числа обратного исходному по порядку входящих в него цифр.'
      f'\nНапример, если введено число 3486, то в результате функция выводит число 6843.')
print(f'Исходное число: {NUMBER}')
print(f'Результат работы обычной функции: {func_revers_number(NUMBER)}')
print(f'Результат работы рекурсивной функции: {rec_reverse_number(NUMBER)}')
print(f'Результат работы оптимизированной рекурсивной функции: {mem_reverse_number(NUMBER)}')

time_func_revers_number = timeit.timeit("func_revers_number(NUMBER)",
                                        setup="from __main__ import func_revers_number, NUMBER",
                                        number=100000)

time_rec_reverse_number = timeit.timeit("rec_reverse_number(NUMBER)",
                                        setup="from __main__ import rec_reverse_number, NUMBER",
                                        number=100000)

mem_reverse_number = timeit.timeit("mem_reverse_number(NUMBER)",
                                   setup="from __main__ import mem_reverse_number, NUMBER",
                                   number=100000)

print('\nЗатраченное время (в милисекундах) на исполнение с помощью'
      f'\n{"- цикла:":25}'
      f' {time_func_revers_number}'
      f'\n{"- рекурсии:":25}'
      f' {time_rec_reverse_number}'
      f'\n{"- рекурсия + мемоизация:":25}'
      f' {mem_reverse_number}')

""" Задача 2 """
"""
Функция подсчета сколько раз встречается определенная цифра в последовательности чисел.
"""


def count_number(number, find_number=0):
    """
    :param number: последовательность чисел
    :param find_number: искомая цифра
    :return: количество определеннаой цифры в последовательности чисел
    """
    count_num = 0
    if len(number) != 0:
        for el in number:
            num = el
            while True:
                num, buffer_num = num // 10, num % 10
                if buffer_num == find_number:
                    count_num += 1
                if num == 0:
                    break
    return count_num


"""
Рекурсивная функция подсчета сколько раз встречается определенная цифра
в последовательности чисел.
"""


def recursion_count_num(count, find_number, num, index=0):
    """
    :param number: последовательность чисел
    :param index: номер числа в последовательности
    :param count: количество определеннаой цифры в последовательности чисел
    :param find_number: искомая цифра
    :param num: очередное число последовательности
    :return: количество определеннаой цифры в последовательности чисел
    """
    buffer_num = num % 10
    if buffer_num == find_number:
        count += 1
    if num == 0 and index == len(NUMBER) - 1:
        return count
    elif num == 0:
        return recursion_count_num(count, find_number, NUMBER[index + 1], index + 1)
    else:
        return recursion_count_num(count, find_number, num // 10, index)


# Функция мемоизации для рекурсивной функции "recursion_count_num"
# как способ оптимизации, при котором сохраняется результат выполнения функции
# и этот результат используется при следующем вызове
def memoization_count_num(function):
    """
    Функция мемоизации для рекурсивной функции "rec_reverse_number"
    как способ оптимизации, при котором сохраняется результат выполнения функции
    и этот результат используется при следующем вызове

    :param function: рекурсивная функция
    :return: сохраненный результат
    """
    cache = {}

    def decorate(*args, **kwargs):
        key = (tuple(args), hash(tuple(sorted(kwargs.items()))))
        if key not in cache:
            cache[key] = function(*args, **kwargs)
        return cache[key]

    return decorate


@memoization_count_num
def mem_count_number(count, find_number, num, index=0):
    buffer_num = num % 10
    if buffer_num == find_number:
        count += 1
    if num == 0 and index == len(NUMBER) - 1:
        return count
    elif num == 0:
        return recursion_count_num(count, find_number, NUMBER[index + 1], index + 1)
    else:
        return recursion_count_num(count, find_number, num // 10, index)


del NUMBER
NUMBER = []
for _ in range(10):
    NUMBER.append(int(random.random() * pow(5, 9)))
FIND_NUMBER = random.randint(1, 9)
print(f'\n*********************************** Задача 2 ***********************************'
      f'\nПосчитать сколько раз встречается определенная цифра в последовательности чисел.')
print(f'\nПоследовательность чисел: {NUMBER}')
print(f'Искомая цифра: {FIND_NUMBER}')
print(f'Результат работы обычной функции: {count_number(NUMBER, FIND_NUMBER)}')
COUNT_NUMBER = 0
print(f'Результат работы рекурсивной функции: {recursion_count_num(COUNT_NUMBER, FIND_NUMBER, NUMBER[0])}')
COUNT_NUMBER = 0
print(f'Результат работы оптимизированной рекурсивной функции:'
      f' {mem_count_number(COUNT_NUMBER, FIND_NUMBER, NUMBER[0])}')

time_count_number = timeit.timeit("count_number(NUMBER, FIND_NUMBER)",
                                  setup="from __main__ import count_number, NUMBER, FIND_NUMBER",
                                  number=100000)
time_recursion_count_num = timeit.timeit("recursion_count_num(COUNT_NUMBER, FIND_NUMBER, NUMBER[0])",
                                         setup="from __main__ import recursion_count_num,"
                                               " NUMBER, COUNT_NUMBER, FIND_NUMBER",
                                         number=100000)

time_mem_count_number = timeit.timeit("mem_count_number(COUNT_NUMBER, FIND_NUMBER, NUMBER[0])",
                                      setup="from __main__ import mem_count_number,"
                                            " NUMBER, COUNT_NUMBER, FIND_NUMBER",
                                      number=100000)

print(f'\nЗатраченное время (в милисекундах) на исполнение с помощью'
      f'\n{"- цикла:":25}'
      f' {time_count_number}'
      f'\n{"- рекурсии:":25}'
      f' {time_recursion_count_num}'
      f'\n{"- рекурсия + мемоизация:":25}'
      f' {time_mem_count_number}')

"""
Итоги по результатам замера времени:
На выполнение приведенных выше задач функции с простым циклом тратят меньше времени, чем рекурсионные функции.
В первой задаче разница по времени между рекурсией и обычным циклом не столь существенна - 30 %,
по сравнению с разницей со второй задачей - рекурсия затрачивает времени более чем в 2 раза больше цикла.
Однако, оптимизированные с помощью мемоизации рекурсионные функции существенно выигрывают по времени
по сравнению с простым циклом и обычной рекурсией.
"""
