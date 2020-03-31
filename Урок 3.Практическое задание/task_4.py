"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
import random

def fun(mass):
    print(f"{mass}")
    # key параметром функции max() является функция, которая вычисляет ключ,
    # который используется для определения того, как ранжировать элементы.
    numb = max(mass, key=mass.count)
    print(f"Число {numb} встречается {mass.count(numb)} раза")


MASS = [random.randint(-100, 100) for i in range(50)]
fun(MASS)