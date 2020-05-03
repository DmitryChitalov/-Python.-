"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""
from collections import Counter, deque

def haffman_al(param):
    k = Counter(param)
    if len(k) == 1:
        return {0: list(k)[0], 1: None}
    sort = sorted(k.items(), key=lambda x: x[1])
    while len(sort) > 1:
        weight = sort[0][1] + sort[1][1]
        element = {0: sort[0][0], 1: sort[1][0]}
        sort = sort[2:]
        for i, item in enumerate(sort):
            if weight <= item[1]:
                sort.insert(i, (element, weight))
                break
        else:
            sort.append((element, weight))
    return sort[0][0]

def haffman_al_1(tree, path=''):
    if not isinstance(tree, dict):
        K[tree] = path
    else:
        haffman_al_1(tree[0], path=f'{path}0')
        haffman_al_1(tree[1], path=f'{path}1')


MY_STR = input('Введите строку - ')
K = {}
haffman_al_1(haffman_al(MY_STR))

print(K)
for el in MY_STR:
    print(K[el], end=' ')