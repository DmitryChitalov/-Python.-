"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""


import collections

s = input('Введите строку для кодирования: ')

def haffman_string(str):
    string = collections.Counter()
    for i in range(len(str)):
        string.update(str[i])
    return string

def haffman_tree(array):
    sorted_array = collections.deque(array.most_common()[::-1])
    if len(sorted_array) != 1:
        while len(sorted_array) > 1:
            weight = sorted_array[0][1] + sorted_array[1][1]
            comb = {0: sorted_array.popleft()[0], 1: sorted_array.popleft()[0]}
            for i, count in enumerate(sorted_array):
                if weight > count[1]:
                    continue
                else:
                    sorted_array.insert(i, (comb, weight))
                    break
            else:
                sorted_array.append((comb, weight))
    else:
        weight = sorted_array[0][1]
        comb = {0: sorted_array.popleft()[0], 1: None}
        sorted_array.append((comb, weight))
    return sorted_array[0][0]




code_table = dict()
def haffman_dict(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_dict(tree[0], path=f'{path}0')
        haffman_dict(tree[1], path=f'{path}1')

haffman_dict(haffman_tree(haffman_string(s)))
print(code_table)


str = []
for i in s:
    str.append(code_table[i])
coded_s = ' '.join(str)
print('Закодированная строка: ')
print(coded_s)



decode_table = dict()
def haffman_decode(code_table, s):
    for k, v in code_table.items():
        decode_table.update({v: k})
    s = s.split(' ')
    print('Декодированная срока: ')
    for i in s:
        print(decode_table[i], end='')

haffman_decode(code_table, coded_s)