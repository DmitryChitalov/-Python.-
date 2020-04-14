import memory_profiler
import time

class DataItem(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

t1 = time.process_time()
m1 = memory_profiler.memory_usage()

data = []
for p in range(100000):
    data.append(DataItem("Alex", 42, "middle of nowhere"))

t2 = time.process_time()
m2 = memory_profiler.memory_usage()
print(f"Выполнение заняло {t2 - t1} сек and {m2[0] - m1[0]} Мб")


class DataItem2(object):
    __slots__ = ['name', 'age', 'address']
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

t11 = time.process_time()
m11 = memory_profiler.memory_usage()

data = []
for p in range(100000):
    data.append(DataItem("Alex", 42, "middle of nowhere"))
    
t22 = time.process_time()
m22 = memory_profiler.memory_usage()
print(f"Выполнение заняло {t22 - t11} сек and {m22[0] - m11[0]} Мб")
'''
Выполнение заняло 0.09375 сек and 10.56640625 Мб
Выполнение заняло 0.09375 сек and 0.703125 Мб

Замер эффективности использования слотов вместо словаря демонстрирует многократное преимущество
в эффективности использования памяти, и, таким образом, убедительно свидетельствует  в пользу
применения слотов для оптимизации кода в случае когда количество параметров аттрибута
известно заранее

'''