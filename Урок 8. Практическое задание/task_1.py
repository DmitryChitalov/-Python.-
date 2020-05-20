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
ready_list = []
d = set()
s = 'трава'
n = len(s)
for i in range(n):
    for y in range(i, n + 1):
        if i == y or i == 0 and y == n:
            continue
        ready_list.append(s[i:y])
        d.add(hashlib.sha1(s[i:y].encode('utf-8')).hexdigest())
print(ready_list)
print(d)
