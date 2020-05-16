"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""
from collections import Counter, deque


def haffman_tree(s):
    count = Counter(s)
    sorted_elems = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(sorted_elems) != 1:
        while len(sorted_elems) > 1:
           
            weight = sorted_elems[0][1] + sorted_elems[1][1]
            
            combined = {0: sorted_elems.popleft()[0],
                    1: sorted_elems.popleft()[0]}

            for i, _count in enumerate(sorted_elems):
                if weight > _count[1]:
                    continue
                else:
                    sorted_elems.insert(i, (combined, weight))
                    break
            else:

                sorted_elems.append((combined, weight))
            
    else:
        weight = sorted_elems[0][1]
        combined = {0: sorted_elems.popleft()[0], 1: None}
        sorted_elems.append((combined, weight))
    return sorted_elems[0][0]


code_table = dict()

def haffman_code(tree, path=''):

    if not isinstance(tree, dict):
        code_table[tree] = path

    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')



s = "winner chicken dinner"

haffman_code(haffman_tree(s))

for i in s:
    print(code_table[i], end=' ')
print()