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

s1 = 'qwerty'
s = s1[:]
l = []
n = len(s)
print(f'Строка: {s1}\nПодстроки:')

while n != 0:
    for i in range(1, len(s) + 1):
        if s[0:i] != s1 and s[0:i] not in l:
            l.append(s[0:i])
            print(s[0:i])
    n -= 1
    s = s[1:]

r = set([hashlib.sha1(el.encode('utf-8')).hexdigest() for el in l])
print(f'Итог: {len(r)} подстрок')
print(r)

del l, s1, s, n
