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

def substring_count(string):
    result = set()
    for i in range(len(string) + 1):
        for el in range(i + 1, len(string) + 1):
            hash_ = hashlib.sha1(string[i:el].encode('utf-8')).hexdigest()
            result.add(hash_)

    result.remove(hashlib.sha1(string.encode('utf-8')).hexdigest())
    count = len(result)
    return f'Количество подстрок в строке "{string}" = {count}'


STRING = 'papa'
print(substring_count(STRING))
