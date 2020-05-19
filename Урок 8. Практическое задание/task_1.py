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

S = input("Введите строку из маленьких латинских букв: ")

substrings = {S[0]: hashlib.sha1(S[0].encode('utf-8')).hexdigest()}
for i in range(1, len(S)):  # длина подстроки
    for j in range(len(S) - i + 1):  # с каких позиций искать подстроку
        substrings[S[j: j + i]] = hashlib.sha1(S[j: j + i].encode('utf-8')).hexdigest()

substrings_count = 0
for keys in substrings.keys():
    print(keys)
    substrings_count += 1

print()
print(f"Итог: {substrings_count} подстрок")
