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
from hashlib import sha1

STR = 'Python3'
my_set = set()

for first_sym in range(len(STR)):
    if first_sym == 0:
        length_sym = len(STR) - 1
    else:
        length_sym = len(STR)
    for last_sym in range(length_sym):
        if last_sym >= first_sym:
            substring = sha1(STR[first_sym:last_sym + 1].encode('utf-8')).hexdigest()
            my_set.add(substring)

print(f'В строке - {STR} - {len(my_set)} подстрок')
