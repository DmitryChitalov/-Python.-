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

user_string = input("Введите строку из маленьких латинских букв: ")
data_set = set()

string_length = len(user_string)
for i in range(string_length):
    if i == 0:
        string_length = len(user_string) - 1
    else:
        string_length = len(user_string)
    for j in range(string_length, i, -1):
        print(user_string[i:j])
        data_set.add(hashlib.sha1(user_string[i:j].encode('utf-8')).hexdigest())
print(data_set)


print("Количество различных подстрок в строке '%s' равно %d" % (user_string, len(data_set)))

