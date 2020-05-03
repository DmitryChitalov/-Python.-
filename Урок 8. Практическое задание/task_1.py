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

MY_STRING = input('Введите строку - ').lower()
NEW_STRING = set()

for i in range(len(MY_STRING)):
	for j in range(i,len(MY_STRING)):
		NEW_STRING.add(hashlib.sha1(MY_STRING[i:j].encode('utf-8')).hexdigest())

print(f'Итого {len(list(NEW_STRING))} подстрок')
