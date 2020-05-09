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

USER_STRING = input("Введите строку латинскими буквами в нижнем регистре: ")
HASH_STOCK = set()

N = len(USER_STRING)

for j in range(N):
    k = USER_STRING[0:N - j]
    for i in range(len(k)):
        print(k[i:N])
        HASH_STOCK.add(hashlib.sha1(k[i:N].encode('utf-8')).hexdigest())
HASH_STOCK.discard(hashlib.sha1(USER_STRING.encode('utf-8')).hexdigest())

print(HASH_STOCK)
print(f"В введенной строке {len(HASH_STOCK)} подстрок")
