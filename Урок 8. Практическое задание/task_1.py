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


STR = 'papa'
# сразу добавляем в список хэшей исходную строку
HASHS = [hashlib.sha1(bytes(STR, encoding='ascii')).hexdigest()]
LEN = len(STR)
UNIQUE = []
for i in range(LEN):
    for j in range(i, LEN):
        string = STR[i:j + 1]
        h = hashlib.sha1(bytes(string, encoding='ascii'))
        if h.hexdigest() not in HASHS:
            HASHS.append(h.hexdigest())
            UNIQUE.append(string)
print(f'В строке "{STR}" имеется {len(UNIQUE)} уникальных подстрок: {UNIQUE}')