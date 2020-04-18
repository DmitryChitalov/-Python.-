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
import collections
from memory_profiler import profile
from sys import getrefcount

ENTERPRISE = collections.namedtuple('Enterprise', ['name', 'q1', 'q2', 'q3', 'q4'])


def input_enterprise():
    """Ввод данных с клавиатуры"""
    iname = input('Введите название предприятия: ')
    iq1 = int(input('Введите прибыль за 1 квартал: '))
    iq2 = int(input('Введите прибыль за 2 квартал: '))
    iq3 = int(input('Введите прибыль за 3 квартал: '))
    iq4 = int(input('Введите прибыль за 4 квартал: '))

    exn = ENTERPRISE(name=iname, q1=iq1, q2=iq2, q3=iq3, q4=iq4)
    return exn
    print(getrefcount(exn))
def annual_revenue(exn: ENTERPRISE):
    """Total"""
    return exn.q1 + exn.q2 + exn.q3 + exn.q4

def calculate(es_new: list):
    """Расчет выше стреднего и ниже среднего занчения"""
    sum_revenue = 0
    for e_new in es_new:
        sum_revenue += annual_revenue(e_new)
    average_revenue = sum_revenue / len(es_new)

    below_avarage = list()
    above_avarage = list()

    for e_new in es_new:
        if annual_revenue(e_new) > average_revenue:
            above_avarage.append(e_new)
        elif annual_revenue(e_new) < average_revenue:
            below_avarage.append(e_new)

    return below_avarage, above_avarage

def solution():
    """Решение задачи"""
    count = int(input('Введите количество предприятий для расчета: '))
    es_new = list()

    for _ in range(count):
        e_new = input_enterprise()
        es_new.append(e_new)

    above_average, below_average = calculate(es_new)

    print("Выше среднего")
    for e_new in above_average:
        print(e_new.name)

    print("Ниже среднего")
    for e_new in below_average:
        print(e_new.name)

@profile
def test():
    """test"""

    enterprises = list()
    for i in range(100000):
        enterprises.append(ENTERPRISE(name="one", q1=i, q2=i, q3=i, q4=i))

    above, below = calculate(enterprises)
    print("Выше среднего", above)
    print("Ниже среднего", below)

    del enterprises
    del above
    del below




# start
#solution()
test()
"""
Line #    Mem usage    Increment   Line Contents
================================================
   74     13.5 MiB     13.5 MiB   @profile
    75                             def test():
    76                                 
    77                             
    78     13.5 MiB      0.0 MiB       enterprises = list()
    79     20.3 MiB      0.1 MiB       for i in range(100000):
    80     20.3 MiB      0.2 MiB           enterprises.append(ENTERPRISE(name="one", q1=i, q2=i, q3=i, q4=i))
           ^^^ Прибавилось 6.9 MiB потому что выделили объекты в цикле.
    81       
    82     20.6 MiB      0.3 MiB       above, below = calculate(enterprises)
           ^^^ Прибавилось 0.3 MiB потому что создали два новых list.
    83     20.6 MiB      0.0 MiB       print("Выше среднего", above)
    84     20.5 MiB      0.0 MiB       print("Ниже среднего", below)
    85                             
    86     20.1 MiB      0.0 MiB       del enterprises
           ^^^ Освободили 0.4 MiB потому что освободили память от list но обьекты остались в above и below.
    87     17.2 MiB      0.0 MiB       del above
           ^^^ Освободили 2.9 MiB потому что освободили память от list и обьектов которые были внутри 
    88     14.0 MiB      0.0 MiB       del below
           ^^^ Освободили 3.2 MiB потому что освободили память от list и обьектов которые были внутри 

    Проблем с памятью нет. Всё в пределах нормы.

(venv) C:\Users\anna\PycharmProjects\Python_Algos>python --version
Python 3.8.2

Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32q

(venv) C:\Users\anna\PycharmProjects\Python_Algos>systeminfo
System Type:               x64-based PC
"""

