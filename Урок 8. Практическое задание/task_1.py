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


string = input("Введите строку из маленьких латинских букв: ")
num = set()

n = len(string)
for i in range(n):
    if i == 0:
        n = len(string) - 1
    else:
        n = len(string)
    for j in range(n, i, -1):
        #print(string[i:j])
        num.add(hashlib.sha1(string[i:j].encode('utf-8')).hexdigest())
#print(num)


print(f"Количество подстрок в строке равно {len(num)}")