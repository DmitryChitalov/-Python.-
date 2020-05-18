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


def unique_substr(s):
    l = len(s)
    substr_hash = set()
    substr = set()
    for i in range(l):
        if i == 0:
            l = len(s) - 1
        else:
            l = len(s)
        for n in range(l, i, -1):
            substr.add(s[i:n])
            substr_hash.add(hashlib.sha1(s[i:n].encode('utf-8')).hexdigest())
    return f'В строке {s} количество уникальных подстрок - {len(substr_hash)}:\n{substr}'


my_str = input('Введите строку из маленьких латинских букв: ')
print(unique_substr(my_str))
