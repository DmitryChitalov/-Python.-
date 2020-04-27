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


def find_num_string(s):
    list_string = []
    len_s = len(s)
    for i in range(len_s):
        list_string.append(hashlib.sha1(s[i].encode('utf-8')).hexdigest())
        for j in range(i + 1, len_s):
            if j == len_s:
                list_string.append(hashlib.sha1(s[i:].encode('utf-8')).hexdigest())
            list_string.append(hashlib.sha1(s[i:j + 1].encode('utf-8')).hexdigest())
    list_string.remove(hashlib.sha1(s.encode('utf-8')).hexdigest())

    return len(set(list_string))


my_string = input('Enter string: ')

print(find_num_string(my_string))
