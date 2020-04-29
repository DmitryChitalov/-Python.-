"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""

import collections


def haffman_dict(inp_str):
    '''создает структуру дерева'''
    counter = collections.Counter(inp_str)
    if len(counter) == 1:
        return {0: list(counter)[0], 1: None}
    counter_sorted = sorted(counter.items(), key=lambda x: x[1])
    while len(counter_sorted) > 1:
        weight = counter_sorted[0][1] + counter_sorted[1][1]
        element = {0: counter_sorted[0][0], 1: counter_sorted[1][0]}
        counter_sorted = counter_sorted[2:]
        for i, item in enumerate(counter_sorted):
            if weight <= item[1]:
                counter_sorted.insert(i, (element, weight))
                break
        else:
            counter_sorted.append((element, weight))
    return counter_sorted[0][0]


def haffman_code(tree, path=''):
    '''формирует словарь кодов Хаффмана'''
    if not isinstance(tree, dict):
        CODES[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


INP_STR = "beep boop beer!"
CODES = {}
haffman_code(haffman_dict(INP_STR))

print(CODES)
for letter in INP_STR:
    print(CODES[letter], end=' ')