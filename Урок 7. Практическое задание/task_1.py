"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

"""Как получается что при вызове функции из timeit с параметром number=10 мы получаем:
[-68, -94, 6, -4, 83, -55, -27, 36, -4, 98] - исходный массив
[98, 83, 36, 6, -4, -4, -27, -55, -68, -94] - отсортированный массив
[98, 83, 36, 6, -4, -4, -27, -55, -68, -94]
[98, 83, 36, 6, -4, -4, -27, -55, -68, -94]
[98, 83, 36, 6, -4, -4, -27, -55, -68, -94]
[98, 83, 36, 6, -4, -4, -27, -55, -68, -94]
[98, 83, 36, 6, -4, -4, -27, -55, -68, -94]
[98, 83, 36, 6, -4, -4, -27, -55, -68, -94]
[98, 83, 36, 6, -4, -4, -27, -55, -68, -94]
[98, 83, 36, 6, -4, -4, -27, -55, -68, -94]
[98, 83, 36, 6, -4, -4, -27, -55, -68, -94]
0.00026380000000000153 - замеренное время выполнения
Получается функция вызывается один раз, сохраняется как объект и выполняется 10-ть раз, или как?
Ведь если бы функция вызывалась все время заново мы бы получали разные массивы"""


from random import randint
from timeit import timeit
from copy import deepcopy

cycle = 1   # параметр number


def sort_1(ary1):    # простая сортировка
    print(ary1)    # исходный массив
    n = 1
    while n < len(ary1):
        for i in range(len(ary1)-n):
            if ary1[i] < ary1[i+1]:
                ary1[i], ary1[i+1] = ary1[i+1], ary1[i]
        n += 1
        # print(ary1)    # если нужно посмотреть сортировку
    return ary1


def sort_2(ary2):    # улучшенная сортировка
    print(ary2)    # исходный массив
    n = 1
    b = 0    # переменная для обозначения сортировки
    while n < len(ary2):
        for i in range(len(ary2)-n):
            if ary2[i] < ary2[i+1]:
                b = 1   # произошла сортировка
                ary2[i], ary2[i+1] = ary2[i+1], ary2[i]
        if b == 0:
            # print(f'n = {n}, break')    # чтобы видеть что произошло прерывание и на каком шаге
            break
        n += 1
        b = 0   # сбрасываем значение перед новым циклом
        # print(ary2)    # если нужно посмотреть сортировку
    return ary2
    # return n      # для подсчета среднего n


ary = [randint(-100, 99) for _ in range(10)]
print(sort_1(deepcopy(ary)), '\n')
print(sort_2(deepcopy(ary)))


"""# функция замера среднего значения n
def func(n):
    x = 0
    for i in range(n):
        ary = [randint(-100, 99) for _ in range(1000)]
        x += sort_2(ary)
    return x / n


print(func(10000))
# среднее значение n = 7.5 при размерре массива = 10
# среднее значение n = 88.75 при размерре массива = 100
# среднее значение n = 959.2 при размерре массива = 1000"""

"""
Пробовал затолкать в цикл замеры, но не получилось сделать импрорт массива ary
не находит его в __main__
'ImportError: cannot import name 'ary' from '__main__' (D:/Prog/Python/GeekBrains/Algorithms/Repositories/Урок 7. Практическое задание/task_1.py)'
а как сделать импорт из функции не разобрался

def timer():
    for i in range(1, 3):
        ary = [randint(-100, 99) for _ in range(10 ^ i)]
        print(ary)
        print(timeit("sort_1(ary)",
                            setup="from __main__ import sort_1, ary", number=1000))"""


# ary = [randint(-100, 99) for _ in range(100)]
# print(timeit("sort_1(ary)",
#                     setup="from __main__ import sort_1, ary", number=cycle))
#
# ary = [randint(-100, 99) for _ in range(1000)]
# print(timeit("sort_1(ary)",
#                     setup="from __main__ import sort_1, ary", number=cycle))
#
# ary = [randint(-100, 99) for _ in range(10000)]
# print(timeit("sort_1(ary)",
#                     setup="from __main__ import sort_1, ary", number=cycle))
#
#
# ary = [randint(-100, 99) for _ in range(100)]
# print(timeit("sort_2(ary)",
#                     setup="from __main__ import sort_2, ary", number=cycle))
#
# ary = [randint(-100, 99) for _ in range(1000)]
# print(timeit("sort_2(ary)",
#                     setup="from __main__ import sort_2, ary", number=cycle))
#
# ary = [randint(-100, 99) for _ in range(10000)]
# print(timeit("sort_2(ary)",
#                     setup="from __main__ import sort_2, ary", number=cycle))

"""Аналитика:
Параметр number=1
0.0016781999999999977   - время выполнения простой сортировки, массив = 100
0.18653530000000001     - время выполнения простой сортировки, массив = 1000
30.1962433              - время выполнения простой сортировки, массив = 10000
0.0016691000000008671   - время выполнения улучшенной сортировки, массив = 100
0.4454394000000015      - время выполнения улучшенной сортировки, массив = 1000
33.3709168              - время выполнения улучшенной сортировки, массив = 10000

Параметр number=10
0.012665999999999997    - время выполнения простой сортировки, массив = 100
1.754571                - время выполнения простой сортировки, массив = 1000
189.11359399999998      - время выполнения простой сортировки, массив = 10000
0.002147199999996019    - время выполнения улучшенной сортировки, массив = 100
0.2006688999999824      - время выполнения улучшенной сортировки, массив = 1000
24.730209700000017      - время выполнения улучшенной сортировки, массив = 10000

Как видим из выше приведенной аналитикивремя при number=10 время выполнения простой сортировки 
увиличилось приблизительно в 10-ть раз по сравнению с замером влемени с number=1.
При этом видно что время выполнения улучшенной сортировки осталось примерно темже при 
параметре number=10 и number=1.
Зи чего можно сделать вывод что при number>1 каждый последующий вызов функции 
получает функцию с уже отсортированным массивом.
Я бы считал что нельзя опираться на замеры данным способом при number>1
По этому ниже привожу несколько замеров с number=1

0.002240099999999995
0.2961099
30.984902599999998
0.0016598999999999364
0.33731519999999904
31.8192015

0.0018780000000000047
0.3827873
37.9028465
0.00626890000000202
0.49634799999999757
38.63009039999999

0.002745499999999998
0.2024433
24.977353700000002
0.0016224999999998602
0.2522155000000019
27.3104785

0.0031039999999999957
0.2616917
25.0748498
0.0025832999999977346
0.2976138999999982
28.2751363

0.001886699999999998
0.1868109
28.2501964
0.002189399999998898
0.20831820000000079
27.357887100000003

Как видно из замеров с number=1 улучшенная сортировка не показывает заметного уменьшения времени выполнения.

С другой стороны если собрать статистику того на каком этапе происходит break (n)
среднее значение n = 7.5 при размерре массива = 10
среднее значение n = 88.75 при размерре массива = 100
среднее значение n = 959.2 при размерре массива = 1000
Из этого можно сделать вывод, что улучшенный алгоритм при малых размерах массива (~10) дает 
небольшой прирост скорости выполнения.
Но при больших размерах массива (~1000) средняя скоросто выполнения уменьшается незначительно.
"""