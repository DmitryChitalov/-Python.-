"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

import math
from timeit import Timer

"""
в данной функции поскольку на каждое простое число p
призодитя n/p итераций то =>
в итоге оценку можно записать как 
сумму по всем p из исходного множества n/p
оценка скорости сводится к оценке суммы 1/p
учитывая оценку p как n/ln(n) то ряд можно заменьть интергалом
в итоге получаем оценку O(N*ln(lnN)) 
при малых N можно аппроксимировать до линейной функции
"""
def eratosfen(n, p):

    if p <= (n/math.log(n)) + 1:
        index = 1
        values = {i: True for i in range(2, n+1)}
        for key in values:
            if values[key]:
                if index == p:
                    return key
                index += 1
                k = 2
                while key*k <= n:
                    values[key*k] = False
                    k += 1
    return f"В данном диапазоне может быть примерно {n// math.log(n) + 1} простых чисел\n" \
           f"Задайте больший диапазон"


"""
в данной функции, поскольку в худшем случае для
простого числа идет обход по всему списку,
то для двойного цикла общую сложность 
можно оценить как O(N^2)
"""
def simple_check(n, p):

    if p <= (n/math.log(n)) + 1:
        index = -1
        values = list(range(2, n))
        simple = []
        for el in values:
            if index == p-1:
                return simple[index]
            check = True
            for number in values:
                if el % number == 0 and el != number:
                    check = False
                    break
            if check:
                simple.append(el)
                index += 1
    return f"В данном диапазоне может быть примерно {n // math.log(n) + 1} простых чисел\n" \
           f"Задайте больший диапазон"


"""
Функция для проведения расчетов и оценки времени
"""
def time_check(start_n=10, stop_n=1000, step=10):
    n = start_n
    with open(f"simple.txt", "w", encoding='utf8') as file:
        file.write("N\tP_Index\tEratosfen\tSimple_Check\n")
        while n <= stop_n:
            p = n // math.log(n) + 1
            t1 = Timer(f"eratosfen({n}, {p})", f"from __main__ import eratosfen")
            t2 = Timer(f"simple_check({n}, {p})", f"from __main__ import simple_check")
            time1 = t1.timeit(number=100)
            time2 = t2.timeit(number=100)
            file.write(f"{n}\t{p}\t{time1}\t{time2}\n")
            n += step


time_check()
# Результаты показывают, что на больших масштабах
# Эффективнее пользоваться решетом Эратосфена
# Поскольку работает быстрее обычного поиска
# Но на малых масштабах это не существенно и
# И можно пользоваться любым из меодов
# Данные взяты изфайла simple.txt
# Общие тенденции представлены в exel файле
#   N = 10	P = 5	time_erat = 0,0003229	time_simple = 0,000412
#   N = 100	P = 22	time_erat = 0,0026565	time_simple = 0,0123347
#   N = 1000 P = 145 time_erat = 0,0403658	time_simple = 0,6435195
