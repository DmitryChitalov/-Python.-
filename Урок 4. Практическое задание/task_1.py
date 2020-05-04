"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

import timeit

NUMBER = "123884906456435435345345345656456546564564562421313133445645766456346345242344667678658765774575"
LEN = len(NUMBER)
NUM = int(NUMBER)
def rev(i, num, newi, newnum):
    if i == 0:
        return #print(f'Перевернутое число: {newnum}')
    else:
        i -= 1
        digit = num // int('1' + i * '0')
        num -= int(str(digit) + i * '0')
        newnum += int(str(digit) + newi * '0')
        rev(i, num, newi+1, newnum)
"""Использую свой алгоритм с рекурсией, не самое быстрое решение
Результат 0.590"""

def cycle_rev(num):
    I = len(num)
    NUM = int(num)
    NewNUM = 0
    NewI = 0
    while I > 0:
        I -= 1
        digit = NUM // int('1' + I * '0')
        NUM -= int(str(digit) + I * '0')
        NewNUM += int(str(digit) + NewI * '0')
        NewI += 1
"""Использую свой алгоритм с циклом
Чуть быстрее 0.497"""

def flip(numb, fliped = 0):
    if numb == 0:
        return #print(fliped)
    else:
        fliped = (fliped*10) + (numb % 10)
        numb = numb // 10
        flip(numb, fliped)
"""Эталонный алгоритм, результат 0.103"""

print(timeit.timeit('rev(LEN, NUM, 0, 0)', setup='from __main__ import rev, NUMBER, LEN, NUM', number=1000))
print(timeit.timeit('cycle_rev(NUMBER)', setup='from __main__ import cycle_rev, NUMBER, LEN, NUM', number=1000))
print(timeit.timeit('flip(NUM)', setup='from __main__ import flip, NUMBER, LEN, NUM', number=1000))
