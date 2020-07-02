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
import cProfile
from timeit import timeit
import sys

sys.setrecursionlimit(1000000)


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        return time.time() - start

    return wrapper()


def sequence_while(N):
    q = -0.5
    start = 1
    _sum = 0

    while N:
        N -= 1
        _sum += start
        start *= q

    return _sum


def memorize(func):
    def wrapper(n, memory=dict()):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r

    return wrapper


# @memorize
def sequence(num, start=1):
    if not num:
        return 0
    return start + sequence(num - 1, start / -2)


N = 0
for _ in range(4):
    print(f'    Работа функции через цикл при N = {N: >5}:', end=' ')
    print(timeit('sequence_while(N)', setup='from __main__ import sequence_while, N', number=10000))
    print(f'Работа функции через рекурсию при N = {N: >5}:', end=' ')
    print(timeit('sequence(N)', setup='from __main__ import sequence, N', number=10000))
    N *= 10

"""    
    Работа функции через цикл при N =    10: 0.009824103999562794
Работа функции через рекурсию при N =    10: 0.0223529659997439
    Работа функции через цикл при N =   100: 0.07789250000132597
Работа функции через рекурсию при N =   100: 0.22804951800026174
    Работа функции через цикл при N =  1000: 0.9066606659998797
Работа функции через рекурсию при N =  1000: 3.901533741000094
    Работа функции через цикл при N = 10000: 9.399621095999464
Работа функции через рекурсию при N = 10000: 74.01455325700044 

Функция sequence_while, реализованная через цикл while,  имеет сложность линейную O(n), так как при каждом увеличении
N в 10 раз, и скорость выполнения увеличивается в 10 раз
Функция sequence, реализованная через рекурсию, имеет сложность O(n^2), так как с каждым увеличением значения N 
в 10 раз, скорость выполнения рекурсивной функции возрастает в 1, 83, 19 (соответственно) раз с каждой итерацией
(время выполнения растет по пораболе вверх)
Функция, выполненная через цикл, отрабатывает быстрее рекурсивной функции в 7,87 раз
Максимальная сложность всего скрипта - O(n^2)

Проверка через профилировщик:
Работа профилировщика на функции с циклом:
         4 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 task_1.py:31(sequence_while)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Функция с циклом отработала без особых проблем.

Работа профилировщика на функции с рекурсией:
         10004 function calls (4 primitive calls) in 0.015 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.015    0.015 <string>:1(<module>)
  10001/1    0.015    0.000    0.015    0.015 task_1.py:56(sequence)
        1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
При работе видны проблемные места при вызове рекурсии и наполнении стека.
"""
# input('Продолжить')

print('Работа cProfile на функции с циклом: ')
cProfile.run('sequence_while(10000)')
print('Работа cProfile на функции с рекурсией: ')
cProfile.run('sequence(10000)')


# input('Второй пример. Продолжить')


def ascii_table(num):
    for char_num in range(32, num + 1):
        if (char_num - 2) % 10 == 0:
            print()
        print(f'{char_num:4} - {chr(char_num)}', end=' ')

    print('\n \n')


def ascii_table_recur(num):
    if num == 32:
        return f' {num:4} - {chr(num)}'
    if (num - 2) % 10 == 0:
        return f'{ascii_table_recur(num - 1)}\n {num:4} - {chr(num)}'
    return f'{ascii_table_recur(num - 1)}{num:4} - {chr(num)}'


# ascii_table()
# print(ascii_table())
# print(ascii_table_recur(127))


@memorize
def ascii_table_2(num):
    if num == 32:
        return f' {num:4} - {chr(num)}'
    if (num - 2) % 10 == 0:
        return f'{ascii_table_2(num - 1)}\n {num:4} - {chr(num)}'
    return f'{ascii_table_2(num - 1)}{num:4} - {chr(num)}'


print()
test1 = timeit('ascii_table(10127)', setup='from __main__ import ascii_table', number=1000)
print('Проверка через функции без рекурсии через timeit:', test1)

test2 = timeit('ascii_table_recur(10127)', setup='from __main__ import ascii_table_recur', number=1000)
print('Проверка через функции с рекурсией через timeit:', test2)

test3 = timeit('ascii_table_2(10127)', setup='from __main__ import ascii_table_2', number=1000)
print('Проверка через функции с рекурсией через timeit c мемоизацией:', test3)

# cProfile.run(ascii_table(127))  # Не разобрался почему не работает

"""
запуск со значением 127
Проверка через функции без рекурсии через timeit: 0.20452959399699466
Проверка через функции с рекурсией через timeit: 0.08252507799988962
Проверка через функции с рекурсией через timeit c мемоизацией: 0.0003578309988370165


запуск со значением 1127
Проверка через функции без рекурсии через timeit: 2.444435010002053
Проверка через функции с рекурсией через timeit: 1.7331255659992166
Проверка через функции с рекурсией через timeit c мемоизацией: 0.0069545219994324725

запуск со значением 10127
Проверка через функции без рекурсии через timeit: 23.930282642002567
Проверка через функции с рекурсией через timeit: 57.2986454109996
Process finished with exit code 139 (interrupted by signal 11: SIGSEGV)  с мемоизацией не выполнилось

Функция без рекурсии имеет линейную сложность O(n), так как при увеличении в 10 раз входных данных - время 
выполнения увеличивается личнейно тоже в 10 раз.
Функция с рекурсией имеет квадратичную сложность O(n^2), так как при увеличении входных данных в десять раз
время выполнения увеличивается в 21 и 33 раза соответственно (не линейно)
Улучшением в данном случае является функция мемоизации, которая применяется как декоратор и уменьшает время 
выполнения в 249 раз - улучшение внушительное (сомнения остаются только по количеству запусков таймит, 
так как возможен вариант заполнения словаря в первый проходи и 999 раз использование уже существующего словаря.
к сожалению тесты проводились внушительное время и проводить повторные значения только из-за мемоизации не стал)

максимальная сложность всего скрипта - квадратичная O(n^2)
"""
