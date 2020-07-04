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

a = 'papa'

set_ = set()

count = 0
for i in range(len(a)):
    for j in range(len(a) + 1):
        if j <= i:
            continue
        _str = a[i:j]
        cache = hashlib.md5(_str.encode()).hexdigest()
        if cache not in set_ and _str != a:
            print(_str)
            count += 1
        set_.add(cache)

print(f'Итог: {count} подстрок')
