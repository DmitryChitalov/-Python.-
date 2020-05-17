"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.
Пример:
строка для кодирования
s = "beep boop beer!"
Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""
from collections import Counter, deque


def haffman_encode(param):
    count_param = Counter(param)
    if len(count_param) == 1:
        return {0: list(count_param)[0], 1: None}
    sort = sorted(count_param.items(), key=lambda x: x[1])
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


def haffman_freq(tree, path=''):
    if not isinstance(tree, dict):
        ENCODE_DICT[tree] = path
    else:
        haffman_freq(tree[0], path=f'{path}0')
        haffman_freq(tree[1], path=f'{path}1')


while True:
    STRING = input('Введите любую строку из трех слов:\n')
    if len(STRING.split()) == 3:
        break
    else:
        print(f'Ошибка ввода строки.\nНеобходимо ввести строку из ТРЕХ слов!')
ENCODE_DICT = {}
haffman_freq(haffman_encode(STRING))

print(f'\nРезультат:')
for alpha in STRING:
    print(f'{ENCODE_DICT[alpha]}', end=' ')

print(f'\n\nКоды символов:')
for key, value in ENCODE_DICT.items():
    print(f'{key} : {value}')
