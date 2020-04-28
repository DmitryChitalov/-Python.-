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

"""
Я считаю, что в примере ответ неверен, так любая строка является подстрокой самой себе:
>>> 'abc'.find('abc')
0
"""

import hashlib
from collections import OrderedDict


def find_substr(string):
    hash_list = OrderedDict()
    for j in range(len(string)):
        for i in range(j + 1, len(string) + 1):
            substr = string[j:i]
            hash_substr = hashlib.sha1(substr.encode('utf-8')).hexdigest()
            if hash_substr not in hash_list.keys():
                hash_list[hash_substr] = substr
    return [str(sub) for sub in hash_list.values()], len(hash_list)


user_string = input('Введи сторку - ')
substr_el, substr_count = find_substr(user_string)
print(f'Эта строка имеет {substr_count} подстрок:')
for el in substr_el:
    print(el)
