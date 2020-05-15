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


def find_substr(s):
    h_lst = []
    s_lst = []

    for i in range(1, len(s)):
        for j in range(len(s) - i + 1):
            hash_sub = hashlib.sha1(s[j:j + i].encode('utf-8')).hexdigest()
            if hash_sub not in h_lst:
                h_lst.append(hash_sub)
                s_lst.append(s[j:j + i])

    if len(s_lst) > 0:
        return f'Substrings: {len(s_lst)} \n{s_lst}'
    return 'Empty string'


s = input('Enter the string: ')
print(find_substr(s))
