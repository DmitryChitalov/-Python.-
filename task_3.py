"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import timeit
import cProfile

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

enter_num = 1000
print(timeit.timeit("revers(enter_num)", setup="from __main__ import revers, enter_num", number=1000))
print(timeit.timeit("revers_2(enter_num)", setup="from __main__ import revers_2, enter_num", number=1000))
print(timeit.timeit("revers_3(enter_num)", setup="from __main__ import revers_3, enter_num", number=1000))
"""
0.0009411999999999962
0.0006379999999999997
0.00040070000000000383 Наиболее быстрая реализация, поскоьку использует индексный доступ к массиву и не выполняет никаких математических вычислений или рекурсии
"""


def main():
    enter_num = 123456789123456789
    print(revers(enter_num))
    print(revers_2(enter_num))
    print(revers_3(enter_num))
    
cProfile.run('main()')
# Время выполнения модулей очень маленькое и на пофилировании его не видно
"""
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
     19/1    0.000    0.000    0.000    0.000 task_3.py:15(revers)
        1    0.000    0.000    0.000    0.000 task_3.py:25(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:33(revers_3)
        1    0.000    0.000    0.001    0.001 task_3.py:49(main)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        3    0.001    0.000    0.001    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""        