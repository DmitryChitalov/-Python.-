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

"""
Задание_1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""


def multiple_1():
    count = 0
    number_list = [i for i in range(2, 1000)]
    for multiple in range(2, 10):
        for el in number_list:
            if el % multiple == 0:
                count += 1
        print(f'В диапазоне 2-99: {count} чисел кратны {multiple}')
        count = 0


# O(n2) – квадратичная сложность

def multiple_2():
    for multiple in range(2, 10):
        multi_list = [i for i in range(2, 1000) if i % multiple == 0]
        print(f'В диапазоне 2-99: {len(multi_list)} чисел кратны {multiple}')


# O(n2) – квадратичная сложность

print(
    timeit.timeit(
        "multiple_1()",
        setup="from __main__ import multiple_1",
        number=1000))

print(
    timeit.timeit(
        "multiple_2()",
        setup="from __main__ import multiple_2",
        number=1000))

"""
Результат:
0.711261525
0.745961497

Генераторы должны выполняться быстрее, чем аналогичный код с циклом for,
но в данном примере получилось немного дольше. Пробовал много раз, 9 из 10
первый код выполняется быстрее. Возможно потому что в первом вывод результата идет через переменную,
а во втором создается дополнительный массив, из-за которого время увеличивается.
"""
"""
2) Определить, какое число в массиве встречается чаще всего
"""


def get_count_1(number_list):
    # O(n2) – квадратичная сложность
    temp_list = number_list[:]
    count = 0
    max_count = 0
    common_num = 0
    while temp_list:
        now_element = temp_list[0]
        for el in temp_list:
            if el == now_element:
                count += 1
        if count > max_count:
            common_num = now_element
            max_count = count
        while now_element in temp_list:
            temp_list.remove(now_element)
        count = 0
    return f'число {common_num} встречается в массиве {number_list} чаще всего'


def get_count_2(lst):
    # O(n2) – квадратичная сложность. Но это не точно, так как я не видел исходных кодов функций
    numb = max(lst, key=lst.count)
    return f'Число {numb} встречается {lst.count(numb)} раз'


NUMBER_LIST = [2, 8, 4, 8, 8, 9, 4, 4, 7, 2, 8, 4, 8, 2, 4, 4, 7]
print(
    timeit.timeit(
        "get_count_1(NUMBER_LIST)",
        setup="from __main__ import get_count_1, NUMBER_LIST",
        number=100000))

print(
    timeit.timeit(
        "get_count_2(NUMBER_LIST)",
        setup="from __main__ import get_count_2, NUMBER_LIST",
        number=100000))

"""
Результат:
1.211289081
0.711925658

Встроенные функции работают быстрее.
"""

"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран.
"""

NUMBER = 5487546586654554548754658665455454875465866545545487


def revers_1(number, n=1, result=''):
    # O(n) – линейная сложность
    if n > number:
        return result
    numeral = number % (10 * n) // n
    result = f'{result}{numeral}'
    return revers_1(number, n * 10, result)


print(
    timeit.timeit(
        "revers_1(NUMBER)",
        setup="from __main__ import revers_1, NUMBER",
        number=100000))


def revers_2(number, n=1, res=''):
    # O(n) – линейная сложность
    while True:
        numeral = number % (10 * n) // n
        n *= 10
        res = f'{res}{numeral}'
        if n > number:
            break
    return f'перевернутое число: {res}'


print(
    timeit.timeit(
        "revers_2(NUMBER)",
        setup="from __main__ import revers_2, NUMBER",
        number=100000))

"""
Результат:
1.057696615
0.805799258
если очень увеличить число 
22.766292425
19.144336706999997
В данной задаче цикл справляется быстрее, чем рекурсия.
"""
