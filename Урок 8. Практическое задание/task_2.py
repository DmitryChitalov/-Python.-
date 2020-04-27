"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""

from collections import Counter


def hoffman_tree(s):
    unique_elem = Counter(s)
    sorted_elem = sorted(unique_elem.items(), key=lambda item: item[1])
    while len(sorted_elem) > 1:
        node_weight = sorted_elem[0][1] + sorted_elem[1][1]
        node = {
            '0': sorted_elem[0][0],
            '1': sorted_elem[1][0]
        }
        del sorted_elem[0]
        del sorted_elem[0]

        for i, elem in enumerate(sorted_elem):
            if node_weight > elem[1]:
                continue
            else:
                sorted_elem.insert(i, (node, node_weight))
                break
        else:
            sorted_elem.append((node, node_weight))
    return sorted_elem[0][0]


def hoffman_table(tree, code=''):
    for i in tree:
        if not isinstance(tree[i], dict):
            table[tree[i]] = f'{code}{i}'
        else:
            hoffman_table(tree[i], f'{code}{i}')


table = {}

string = "beep boop beer!"

hoffman_table(hoffman_tree(string))

coded_string = []
for char in string:
    coded_string.append(table[char])
print(*coded_string)
