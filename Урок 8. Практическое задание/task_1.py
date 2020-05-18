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

my_string = input('Введите строку состоящаю только из маленьких латинских букв:\n')
substrings = set()
for i in range(len(my_string)):
    for j in range(i, len(my_string)):
        substrings.add(hashlib.sha1(my_string[i:j].encode('utf-8')).hexdigest())

print(f'Итог: {len(list(substrings))} подстрок')
