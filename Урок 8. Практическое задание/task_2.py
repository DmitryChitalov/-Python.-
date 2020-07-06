"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""

from collections import Counter, deque

S = "beep boop beer!"
# S = "bbbbbbb"


def haffman_tree(string):
    cnt = Counter(string)
    sort_cnt = deque(sorted(cnt.items(), key=lambda x: x[1]))
    if len(sort_cnt) > 1:
        while len(sort_cnt) > 1:
            weight = sort_cnt[0][1] + sort_cnt[1][1]
            union = ({0: sort_cnt.popleft()[0], 1: sort_cnt.popleft()[0]}, weight)
            for i, elem in enumerate(sort_cnt):
                if elem[1] < weight:
                    continue
                sort_cnt.insert(i, union)
                break
            else:
                sort_cnt.append(union)
    else:
        # Тут можно немного упростить
        return {0: None, 1: sort_cnt[0][0]}
    return sort_cnt[0][0]


code_list = {}


def crawl_tree(sort_cnt, path=''):
    if isinstance(sort_cnt, dict):
        crawl_tree(sort_cnt[0], path=f'{"0"}{path}')
        crawl_tree(sort_cnt[1], path=f'{"1"}{path}')
    else:
        code_list[sort_cnt] = path


def coding(string, res=''):
    crawl_tree(haffman_tree(string))
    for sym in string:
        res = f'{res} {code_list[sym]}'
    return res


print('Результат:', coding(S))
