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

str = input('Введите строку для анализа: ')

substring = {}


def hash_substring(str):
    for i in range(len(str) - 1):
        for n in range(1, len(str) + 1):
            if i < n and str[i:n] != str:
                hash= hashlib.md5(str[i:n].encode())
                substring.update({hash.hexdigest(): str[i:n]})
    return substring


print('Подстроки:')
for i in hash_substring(str).values():
    print(i)
print(f'Итого {len(substring)} строк')