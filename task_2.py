"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, библиотеки) для оптимизации памяти и
доказать! (наглядно, кодом) их эффективность (на примере профилировщика)
"""
from functools import total_ordering
import memory_profiler
from pympler import asizeof
from sys import getsizeof

class Number_1:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        return self.value == other

    def __lt__ (self, other):
        return self.value < other

    def __le__ (self, other):
        return self.value <= other

    def __gt__ (self, other):
        return self.value > other

    def __ge__ (self, other):
        return self.value >= other

@total_ordering
class Number_2:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        return self.value == other

    def __lt__ (self, other):
        return self.value < other


if __name__ == '__main__':

    m1 = memory_profiler.memory_usage()
    num1 = Number_1(5)
    num2 = Number_1(3)
    print(num1 == num2)
    print(num1 < num2)
    print(num1 <= num2)
    print(num1 > num2)
    print(num1 >= num2)
    m2 = memory_profiler.memory_usage()
    print(f"Работа с Number_1 {m2[0] - m1[0]} Мб")
    print(asizeof.asizeof(Number_1))

    m1 = memory_profiler.memory_usage()
    num3 = Number_2(5)
    num4 = Number_2(3)
    print(num3 == num4)
    print(num3 < num4)
    print(num3 <= num4)
    print(num3 > num4)
    print(num3 >= num4)
    m2 = memory_profiler.memory_usage()
    print(f"Работа с Number_1 {m2[0] - m1[0]} Мб")
    print(asizeof.asizeof(Number_1))

"""
Должно оптимизировать, но профилировщик показывает нули.

"""