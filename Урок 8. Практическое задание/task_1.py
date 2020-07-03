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


def doit(my_string):
    my_set = set()
    for start in range(len(my_string)):
        for finish in range(start + 1, 1 + len(my_string)):
            my_set.add(hashlib.sha3_512(my_string[start:finish].encode('utf-8')).hexdigest())
    return len(my_set) - 1


print('Кол-во уникальных подстрок: ', doit('мама мыла раму'))