"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""

from collections import Counter, deque

def tree_by_haffman(string_for_hashing):
    counts = Counter(string_for_hashing)
    sorted_elements = deque(sorted(counts.items(), key=lambda item: item[1]))
    if len(sorted_elements) != 1:
        while len(sorted_elements) > 1:
            el_weight = sorted_elements[0][1] + sorted_elements[1][1]
            combination = {0: sorted_elements.popleft()[0],
                    1: sorted_elements.popleft()[0]}
            for i, _count in enumerate(sorted_elements):
                if el_weight > _count[1]:
                    continue
                else:
                    sorted_elements.insert(i, (combination, el_weight))
                    break
            else:
                sorted_elements.append((combination, el_weight))
    else:
        el_weight = sorted_elements[0][1]
        combination = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((combination, el_weight))
    return sorted_elements[0][0]


table_of_hashes = dict()

def hash_by_haffman(tree, path=''):
    if not isinstance(tree, dict):
        table_of_hashes[tree] = path
    else:
        hash_by_haffman(tree[0], path=f'{path}0')
        hash_by_haffman(tree[1], path=f'{path}1')


#string_for_hashing = "beep boop beer!"
string_for_hashing = input("Введите строку для хэширования: ")


hash_by_haffman(tree_by_haffman(string_for_hashing))

for i in string_for_hashing:
    print(table_of_hashes[i], end=' ')
print()
