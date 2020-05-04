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
import cProfile
import timeit

target = int(input('Введите номер простого числа: '))

def simple_n(target, simple=[]):
    for i in range(2, 1000000000):
        k = 0
        for x in range(2, i):
            if i % x == 0:
                k += 1
        if k == 0:
            simple.append(i)
        if len(simple) == target:
            break
    return #print(f'{target}-ое простое число: {simple[-1]}')
"""
Результат для 100-го простого числа  0.019 seconds
Результат для 500-го простого числа  1.053 seconds
Результат для 1000-го простого числа 5.615 seconds
Результат для 2000-го простого числа 29.064 seconds
Самый простой и медленный алгоритм. 
Ищем количество делителей у числа из диапазона от 2 до самого числа невключительно,
если таковых нет - объявляем простым числом
Предположительная сложность 2n2"""


def simple_n1(target, simple=[]):
    for i in range(2, 1000000000):
        for x in range(2, i):
            if i % x == 0:
                break
        else:
            simple.append(i)
        if len(simple) == target:
            break
    return #print(f'{target}-ое простое число: {simple[-1]}')
"""
Результат для 100-го простого числа  0.004 seconds
Результат для 500-го простого числа  0.170 seconds
Результат для 1000-го простого числа 0.671 seconds
Результат для 2000-го простого числа 3.169 seconds
Перестаем искать количество делителей, если находим хотя бы один - движемся дальше.
Почти на порядок быстрее предыдущего
Предположительная сложность n2"""

def simple_n2(target, simple=[]):
    for i in range(2, 1000000000):
        for x in simple:
            if i % x == 0:
                break
        else:
            simple.append(i)
        if len(simple) == target:
            break
    return #print(f'{target}-ое простое число: {simple[-1]}')
"""
Результат для 100-го простого числа 0.0024 seconds
Результат для 500-го простого числа 0.0353 seconds
Результат для 1000-го простого числа 0.081 seconds
Результат для 2000-го простого числа 0.331 seconds
Используем только простые числа в качестве делителя 
Почти на порядок быстрее предыдущего
Предположительная сложность n2"""

def simple_n3(target, simple=[]):
    for i in range(2, 1000000000):
        if (i > 10):
            if (i % 2 == 0) or (i % 10 == 5):
                continue
        for x in simple:
            if i % x == 0:
                break
        else:
            simple.append(i)
        if len(simple) == target:
            break
    return #print(f'{target}-ое простое число: {simple[-1]}')
"""
Результат для 100-го простого числа 0.0024 seconds
Результат для 500-го простого числа 0.0337 seconds
Результат для 1000-го простого числа 0.079 seconds
Результат для 2000-го простого числа 0.323 seconds
Данная оптимизация становится актуальна при поиске простых чисел с индексами больше 100,
но стабильного прироста не показывает
Предположительная сложность n2"""

def simples():
    a = 2
    while True:
        for i in range(2, a):
            if a % i == 0:
                break
        else:
            yield a
        a += 1


def simples_n(target, simple=0):
    i = 0
    num = simples()
    while i != target:
        simple = next(num)
        i += 1
    #print((f'{target}-ое простое число: {simple}'))

"""
Результат для 2000-го простого числа 3.008 seconds
Данный алгоритм не обладает преимуществами, медленный, сложный"""


cProfile.run('simple_n(target)')
cProfile.run('simple_n1(target)')
cProfile.run('simple_n2(target)')
cProfile.run('simple_n3(target)')
cProfile.run('simples_n(target)')


#print(timeit.timeit('simple_n2(target)', setup='from __main__ import simple_n2, target', number=10000))
#print(timeit.timeit('simple_n3(target)', setup='from __main__ import simple_n3, target', number=10000))
#print(timeit.timeit('simples_n(target)', setup='from __main__ import simples_n, simples, target', number=1000))
