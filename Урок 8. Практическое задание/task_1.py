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

user_input = input('Введите строку: ')
result = set()
for i in range(0, len(user_input) + 1):
    for j in range(i + 1, len(user_input) + 1):
        result.add(sha1(user_input[i:j].encode('utf-8')).hexdigest())
result.remove(sha1(user_input.encode('utf-8')).hexdigest())  # удалим из множества введенную строку
print(f'Колличество различных подстрок в строке "{user_input}" равно {len(result)}')
