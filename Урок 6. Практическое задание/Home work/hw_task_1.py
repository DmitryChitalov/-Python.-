from random import randint
from timeit import Timer
import memory_profiler

mass = [randint(1, 100) for _ in range(10000)]


# 1_1
def first():
    plase_1 = memory_profiler.memory_usage()
    mass_1 = list(mass)
    answ = [idx for idx in range(len(mass_1)) if mass_1[idx] % 2 == 0]
    plase_2 = memory_profiler.memory_usage()
    answ_1 = plase_2[0] - plase_1[0]
    return answ_1


# 1_2
def second():
    plase_1 = memory_profiler.memory_usage()
    mass_2 = list(mass)
    answ = []
    for idx in range(len(mass_2)):
        if mass_2[idx] % 2 == 0:
            answ.append(idx)
    plase_2 = memory_profiler.memory_usage()
    answ_2 = plase_2[0] - plase_1[0]
    return answ_2


'''-------'''

# 2
def third():
    plase_1 = memory_profiler.memory_usage()
    mass = [randint(-100, 100) for _ in range(10000)]
    len_mass = len(mass)
    number = mass[0]
    max_count = 1
    for el_idx in range(len_mass - 1):
        count = 1
        for idx in range(el_idx + 1, len_mass):
            if mass[el_idx] == mass[idx]:
                count += 1
        if count > max_count:
            max_count = count
            number = mass[el_idx]

    plase_2 = memory_profiler.memory_usage()
    answ_3 = plase_2[0] - plase_1[0]
    return answ_3

# 3
def last():
    plase_1 = memory_profiler.memory_usage()
    answ = []

    for kr in range(2, 10):
        count = 0
        for el in range(2, 100):
            if el % kr == 0:
                count += 1
        answ.append(count)
    for el in range(2, 10):
        continue
        # print(f'В диапазоне 2-99: {answ[el - 2]} чисел кратны {el} ')
    plase_2 = memory_profiler.memory_usage()
    answ_4 = plase_2[0] - plase_1[0]
    return answ_4






print(f'Память затребованая для 1-й: {first()}')
print(f'Память затребованая для 1-й c другим решением: {second()}')
print(f'Память затребованая для 2-й: {third()}')
print(f'Память затребованая для 3-й: {last()}')

'''
Память затребованая для 1-й: 0.12890625 - с генератором
Память затребованая для 1-й c другим решением: 0.0 - обычный цикл
Память затребованая для 2-й: 0.0 - оценка времени работы 2-й задачи.
Память затребованая для 3-й: 0.0 - оценка времени работы 3-й задачи.


1-ю задачу оптимизировал с помощью генератора, так как он работает быстрее.
2-ю и 3-ю задачи не придумал, как улучшить, так как генераторы не поддерживают такой синтаксис...
'''