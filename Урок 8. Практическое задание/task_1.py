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
import timeit


def count_string_hash(s: str):
    set_hash = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            set_hash.add(hash(s[i:j]))
    return len(set_hash) - 1


user_str = 'qewtyqwreytquwuejvdasbvxajhsdv'
print(f'В строке: {user_str} {count_string_hash(user_str)} подстрок')
print(timeit.timeit('count_string_hash(user_str)', number=100, globals=globals()))  # 0.035650877


def count_string_sha(s: str):
    set_sha = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            set_sha.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
    return len(set_sha) - 1


user_str_1 = 'qewtyqwreytquwuejvdasbvxajhsdv'
print(f'В строке: {user_str} {count_string_sha(user_str_1)} подстрок')
print(timeit.timeit('count_string_sha(user_str)', number=100, globals=globals()))  # 0.124520796

"""судя по замерам в данном случае эффективней работает алгоритм со встроенной функцией hash"""
