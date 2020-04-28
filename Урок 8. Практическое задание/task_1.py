"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.

Пример:
строка: рара

подстроки:
рар
ра
р
а
ар
ара

Итог: 6 подстрок
"""
import hashlib
from Tree import Tree


def find_substrings(string):
    """
    :param string: Исходная строка
    :return: Уникальные подстроки и их количество
    """
    data = Tree()
    substrings = []
    i = 0
    while i < len(string):
        s = ''
        for el in range(i, len(string)):
            s += string[el]
            if s != string:
                h_3 = hashlib.sha1(bytes(s, encoding='utf8'))
                if data.find(h_3.hexdigest()) is None:
                    data.append(h_3.hexdigest())
                    substrings.append(s)
        i += 1
    data.show_tree(data_only=False)
    return f'\n\033[32m substrings\033[0m = \033[31m{substrings}\033[0m,' \
           f' \033[32m total_number\033[0m = \033[31m{len(substrings)}'


print(find_substrings("papa"))
