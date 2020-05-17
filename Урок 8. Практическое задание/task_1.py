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

def substr_count(S):

    N = len(S)
    MY_SET = set()

    for i in range(N):
        for j in range(N, i, -1):
            S_1 = S[i:j]
            S_2 = hashlib.sha1(S_1.encode("utf-8"))
            S_3 = S_2.hexdigest()
            MY_SET.add(S_3)
    MY_SET.remove(hashlib.sha1(S.encode("utf-8")).hexdigest())
    return len(MY_SET)

S = input("Введите строку: ")
print(f"Количество подстрок в строке {S}: {substr_count(S)}.")





