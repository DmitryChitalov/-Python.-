"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""
from collections import Counter, deque

my_str = input('Введите строку из трех слов: ')

def tree(new_str):
    count_str = Counter(new_str)
    sort_el = deque(sorted(count_str.items(), key=lambda item: item[1]))
    if len(sort_el) != 1:
        while len(sort_el) > 1:
            sum_freq = sort_el[0][1] + sort_el[1][1]
            union_el = {0: sort_el.popleft()[0], 1: sort_el.popleft()[0]}
            for i, count in enumerate(sort_el):
                if sum_freq > count[1]:
                    continue
                else:
                    sort_el.insert(i, (union_el, sum_freq))
                    break
            else:
                sort_el.append((union_el, sum_freq))
    else:
        sum_freq = sort_el[0][1]
        union_el = {0: sort_el.popleft()[0], 1: None}
        sort_el.append((union_el, sum_freq))
    return sort_el[0][0]

table = dict()

def write_code(tree, path=''):
    if not isinstance(tree, dict):
        table[tree] = path
    else:
        write_code(tree[0], path=f'{path}0')
        write_code(tree[1], path=f'{path}1')


write_code(tree(my_str))

print(list(table.values()))