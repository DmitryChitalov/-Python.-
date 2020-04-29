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
from itertools import combinations


def num_of_substring(s):
    """
    Функция принимает на вход строку и определяет кол-во подстрок
    """
    # Определяем хэш строки
    s_hash = hashlib.sha1(s.encode('utf-8')).hexdigest()
    # Множества для подстрок и их хешей
    sub_str = set()
    sub_hash = set()
    # Определение с помощью функции combinations всех подстрок в строке
    for x, y in combinations(range(len(s) + 1), 2):
        if s[x:y] != " ":
            sub_str.add(s[x:y])
        else:
            continue
    # Определение хешей подстрок
    for item in sub_str:
        h = hashlib.sha1(item.encode('utf-8')).hexdigest()
        sub_hash.add(h)
    # Удаление из множества хеша строки
    sub_hash.remove(s_hash)
    # Удаление из множества исходной строки
    sub_str.remove(s)
    # Вывод подстрок
    for i in sub_str:
        print(i, end="\n")
    return f"Итог: {len(sub_hash)} подстрок"


S = input("Строка: ")
print(num_of_substring(S))
