from random import randint
from timeit import Timer

mass = [randint(1, 100) for _ in range(50)]


# 1_1
def first():
    mass_1 = list(mass)
    answ = [idx for idx in range(len(mass_1)) if mass_1[idx] % 2 == 0]
    # print(answ)


# 1_2
def second():
    mass_2 = list(mass)
    answ = []
    for idx in range(len(mass_2)):
        if mass_2[idx] % 2 == 0:
            answ.append(idx)
    # print(answ)


'''-------'''

# 2
def third():
    mass = [randint(-100, 100) for _ in range(50)]
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

    # print(f'{max_count} раз встречается число - {number}')

# 3
def last():
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



timer_1 = Timer('first()', 'from __main__ import first')
print(f'Firs funk {timer_1.timeit(number=1000)}')
timer_2 = Timer('second()', 'from __main__ import second')
print(f'Second funk {timer_2.timeit(number=1000)}')
timer_3 = Timer('third()', 'from __main__ import third')
print(f'Third funk {timer_3.timeit(number=1000)}')
timer_4 = Timer('last()', 'from __main__ import last')
print(f'Last funk {timer_4.timeit(number=1000)}')

'''
Firs funk 0.013879299999999997 - с генератором
Second funk 0.015675399999999992 - обычный цикл
Third funk 0.2065408 - оценка времени работы 2-й задачи.
Last funk 0.0495951 - оценка времени работы 3-й задачи.


1-ю задачу оптимизировал с помощью генератора, так как он работает быстрее.
2-ю и 3-ю задачи не придумал, как улучшить, так как генераторы не поддерживают такой синтаксис...
'''