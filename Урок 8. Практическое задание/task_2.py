"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""

from collections import Counter, deque

def haffman_tree(my_str):

    frq_count = Counter(my_str)
    frq = deque(sorted(frq_count.items(), key=lambda i: i[1]))

    if len(frq) != 1:
        while len(frq) > 1:
            weight = frq[0][1] + frq[1][1]
            united_el = {0: frq.popleft()[0], 1: frq.popleft()[0]}
            for i, _frequency in enumerate(frq):
                if weight > _frequency[1]:
                    continue
                else:
                    frq.insert(i, (united_el, weight))
                    break
            else:
                frq.append((united_el, weight))
    else:
        weight = frq[0][1]
        united_el = {0: frq.popleft()[0], 1: None}
        frq.append((united_el, weight))
    return frq[0][0]

haffman_table = dict()

def haffman_code(tree, code=''):

    if not isinstance(tree, dict):
        haffman_table[tree] = code
    else:
        haffman_code(tree[0], code=f'{code}0')
        haffman_code(tree[1], code=f'{code}1')


my_str = input("Введите строку из трех слов для кодирования: ")
haffman_code(haffman_tree(my_str))

for i in my_str:
    print(haffman_table[i], end=' ')
print()
