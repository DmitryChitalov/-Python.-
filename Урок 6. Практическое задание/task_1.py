"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from sys import getsizeof
from timeit import timeit
from memory_profiler import profile


def num_generator():
    i = 2
    while True:
        yield i
        i += 1


def get_elem_i(func):
    def wrapper(*args, **kwargs):
        i = kwargs.get('i')
        a = func(*args, **kwargs)
        return a[i - 1]

    return wrapper


def modify_list(func):
    def wrapper(*args, **kwargs):
        i = kwargs.get('i')
        _list = get_list(i)
        a = func(_list, **kwargs)
        return a[i - 1]

    return wrapper


# @get_elem_i
@profile
# @modify_list
def eratosfen(input_list, **kwargs):
    _list = list(input_list)[:]
    for divider in _list:
        for divided in _list:
            if divider != divided and divided % divider == 0:
                _list.remove(divided)
    return _list


# @get_elem_i
@profile
# @modify_list
def linear_simple(input_list, **kwargs):
    """Решение без метода решета Эратосфена, можно передать генератор"""

    simple_list = [2]
    for divider in input_list:
        count = 0
        for divided in simple_list:
            if divider != divided and divider % divided == 0:
                count += 1
        if not count:
            simple_list.append(divider)
    return simple_list[1:]


def get_list(i):  # генерю каждый раз исключительно для тестов
    _len = i * 10
    _list = [item for item in range(2, _len + 1)]
    return _list


@profile
def get_list(i):
    _len = i * 10
    _list = [item for item in range(2, _len + 1)]
    return _list


@profile
def get_set(i):
    _len = i * 10
    _list = {item for item in range(2, _len + 1)}
    return _list


@profile
def get_tuple(i):
    _len = i * 10
    _list = (item for item in range(2, _len + 1))
    final_list = tuple(_list)
    return final_list


@profile
def get_next_tuple(i):
    _len = i * 10
    _list = (item for item in range(2, _len + 1))
    return _list


# get_list(100000)
# get_set(100000)
# get_tuple(100000)
# get_next_tuple(100000)
# print(linear_simple(get_tuple(100)))
# print(linear_simple(get_list(100)))
get_tuple(100000)
# i_elem = 100
# len_list = i_elem * 10
# list_a = [item for item in range(2, len_list + 1)]
# list_f = list_a[:]
# list_b = list(range(len_list + 1)[2:])
# list_c = (item for item in range(2, len_list + 1))
# list_d = {item for item in range(2, len_list + 1)}
# list_e = num_generator()

# print(linear_simple(list_b))
# print(linear_simple(list_f, i=i_elem))
# print(linear_simple(i=1))
# print(linear_simple(i=10))
# print(linear_simple(i=100))
# print(linear_simple(i=1000))
# print(eratosfen(list_a, i=i_elem))
# print(eratosfen(i=1))
# print(eratosfen(i=10))
# print(eratosfen(i=100))
# print(eratosfen(i=1000))

# print(timeit('eratosfen(list_a, 1)', setup='from __main__ import eratosfen')

"""
заволнение списка на 1000000 элементов заняло в 38,6 мебибайта памяти. 
Line #    Mem usage    Increment   Line Contents
================================================
    81     32.4 MiB     32.4 MiB   @profile
    82                             def get_list(i):
    83     32.4 MiB      0.0 MiB       _len = i * 10
    84     71.0 MiB      0.3 MiB       _list = [item for item in range(2, _len + 1)]
    85     71.0 MiB      0.0 MiB       return _list


заполнение множества на 1000000 элементов заняло 77,3 мб памяти! это в 2 раза больше, чем список (думал что список
занимает больше)
при этом 
Line #    Mem usage    Increment   Line Contents
================================================
    88     32.7 MiB     32.7 MiB   @profile
    89                             def get_set(i):
    90     32.7 MiB      0.0 MiB       _len = i * 10
    91    110.0 MiB     16.1 MiB       _list = {item for item in range(2, _len + 1)}
    92    110.0 MiB      0.0 MiB       return _list



заполнение кортежа на 1000000 элементов увеличило 39,7 памяти программы.
при этом графа  Increment показывает 1.6 мебибайт увеличения памяти.
Line #    Mem usage    Increment   Line Contents
================================================
    95     32.5 MiB     32.5 MiB   @profile
    96                             def get_tuple(i):
    97     32.5 MiB      0.0 MiB       _len = i * 10
    98     72.2 MiB      1.6 MiB       _list = (item for item in range(2, _len + 1))
    99     71.8 MiB      0.0 MiB       final_list = tuple(_list)
   100     71.8 MiB      0.0 MiB       return final_list


Line #    Mem usage    Increment   Line Contents
================================================
    81     32.4 MiB     32.4 MiB   @profile
    82                             def get_list(i):
    83     32.4 MiB      0.0 MiB       _len = i * 10
    84     32.8 MiB      0.3 MiB       _list = [item for item in range(2, _len + 1)]
    85     32.8 MiB      0.0 MiB       return _list


Filename: /home/aronsx/GeekBrains/Python_Algos/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    47     32.8 MiB     32.8 MiB   @profile
    48                             # @modify_list
    49                             def eratosfen(input_list, **kwargs):
    50     32.8 MiB      0.0 MiB       _list = input_list[:]
    51     32.8 MiB      0.0 MiB       for divider in _list:
    52     32.8 MiB      0.0 MiB           for divided in _list:
    53     32.8 MiB      0.0 MiB               if divider != divided and divided % divider == 0:
    54     32.8 MiB      0.0 MiB                   _list.remove(divided)
    55     32.8 MiB      0.0 MiB       return _list

************************************************
Далее я запустл код и увидел, что сам код не дает увеличения памяти. 
Память занимает переменная, в которую передается список.
Для оптимизации функции расчета простых чисел не по алгоритму Эратосфена - можно передать генератор

Line #    Mem usage    Increment   Line Contents
================================================
    81     32.4 MiB     32.4 MiB   @profile
    82                             def get_list(i):
    83     32.4 MiB      0.0 MiB       _len = i * 10
    84     32.8 MiB      0.3 MiB       _list = [item for item in range(2, _len + 1)]
    85     32.8 MiB      0.0 MiB       return _list



Line #    Mem usage    Increment   Line Contents
================================================
    47     32.8 MiB     32.8 MiB   @profile
    48                             # @modify_list
    49                             def eratosfen(input_list, **kwargs):
    50     32.8 MiB      0.0 MiB       _list = input_list[:]
    51     32.8 MiB      0.0 MiB       for divider in _list:
    52     32.8 MiB      0.0 MiB           for divided in _list:
    53     32.8 MiB      0.0 MiB               if divider != divided and divided % divider == 0:
    54     32.8 MiB      0.0 MiB                   _list.remove(divided)
    55     32.8 MiB      0.0 MiB       return _list
************************************************

Process finished with exit code 0

Line #    Mem usage    Increment   Line Contents
================================================
    96     32.4 MiB     32.4 MiB   @profile
    97                             def get_tuple(i):
    98     32.4 MiB      0.0 MiB       _len = i * 10
    99     32.4 MiB      0.0 MiB       _list = (item for item in range(2, _len + 1))
   100     32.4 MiB      0.0 MiB       return _list



Line #    Mem usage    Increment   Line Contents
================================================
    47     32.4 MiB     32.4 MiB   @profile
    48                             # @modify_list
    49                             def eratosfen(input_list, **kwargs)
    50     32.7 MiB      0.3 MiB       input_list = list(input_list)  # на этой строке я ожидал сильного прироста памяти
    51     32.9 MiB      0.3 MiB       _list = input_list[:]  # и тут я делаю копию, что не очень эффективно по памяти
    52     32.9 MiB      0.0 MiB       for divider in _list:
    53     32.9 MiB      0.0 MiB           for divided in _list:
    54     32.9 MiB      0.0 MiB               if divider != divided and divided % divider == 0:
    55     32.9 MiB      0.0 MiB                   _list.remove(divided)
    56     32.9 MiB      0.0 MiB       return _list

************************************************
Line #    Mem usage    Increment   Line Contents
================================================
    96     32.4 MiB     32.4 MiB   @profile
    97                             def get_tuple(i):
    98     32.4 MiB      0.0 MiB       _len = i * 10
    99     32.4 MiB      0.0 MiB       _list = (item for item in range(2, _len + 1))
   100     32.4 MiB      0.0 MiB       return _list


Filename: /home/aronsx/GeekBrains/Python_Algos/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    47     32.4 MiB     32.4 MiB   @profile
    48                             # @modify_list
    49                             def eratosfen(input_list, **kwargs):
    50     32.7 MiB      0.3 MiB       input_list = list(input_list)
    51     32.9 MiB      0.3 MiB       _list = input_list[:]
    52     32.9 MiB      0.0 MiB       for divider in _list:
    53     32.9 MiB      0.0 MiB           for divided in _list:
    54     32.9 MiB      0.0 MiB               if divider != divided and divided % divider == 0:
    55     32.9 MiB      0.0 MiB                   _list.remove(divided)
    56     32.9 MiB      0.0 MiB       return _list
************************************************

Основная память затрачивается на сам список. Функция потребляет мало памяти. 
Line #    Mem usage    Increment   Line Contents
================================================
    81     32.4 MiB     32.4 MiB   @profile
    82                             def get_list(i):
    83     32.4 MiB      0.0 MiB       _len = i * 10
    84     32.4 MiB      0.0 MiB       _list = [item for item in range(2, _len + 1)]
    85     32.4 MiB      0.0 MiB       return _list



Line #    Mem usage    Increment   Line Contents
================================================
    59     32.4 MiB     32.4 MiB   @profile
    60                             # @modify_list
    61                             def linear_simple(input_list, **kwargs):
    62                                 '''Решение без метода решета Эратосфена, можно передать генератор'''
    63                             
    64     32.4 MiB      0.0 MiB       simple_list = [2]
    65     32.4 MiB      0.0 MiB       for divider in input_list:
    66     32.4 MiB      0.0 MiB           count = 0
    67     32.4 MiB      0.0 MiB           for divided in simple_list:
    68     32.4 MiB      0.0 MiB               if divider != divided and divider % divided == 0:
    69     32.4 MiB      0.0 MiB                   count += 1
    70     32.4 MiB      0.0 MiB           if not count:
    71     32.4 MiB      0.0 MiB               simple_list.append(divider)
    72     32.4 MiB      0.0 MiB       return simple_list[1:]



Process finished with exit code 0

Подведу итог:
Самый затратный из тестирумых типов данных - моножество, за ним следует список, потом кортеж
Для оптимизации linear_simple я сделал возможность дать на ввод генератор, тем самым сократил использование памяти
Алгоритм Эратосфена изначально работает со списком и убирает данные из него, сохранить логику и передать генератор 
не нашел возможности

Алгоритм Эратосфена работает быстрее, но более ресурсоемкий, 
linear_simple работает дольше, но менее требователен к памяти, благодаря работе с генератором.


64 битная ос, python3.6
"""
