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


def substrings(user_str):
    """Функция подсчёта подстрок в строке"""
    set_substrings = set()
    count = len(user_str)
    for _ in range(len(user_str)):
        for i in range(len(user_str)):
            if user_str not in user_str[i:i+count]:
                set_substrings.add(hashlib.sha256(user_str[i:i+count].encode('utf-8')).hexdigest())
        count -= 1
    return set_substrings


try:
    USER_STR = input("Введите строку состоящую только из маленьких латинских букв: ")
    if not USER_STR.islower():
        raise ValueError("Строка не в нижнем регистре!")
    elif not USER_STR.isalpha():
        raise ValueError("В строке не только маленькие буквы!")
    print(f"Количество подстрок: {len(substrings(USER_STR))}\nХэши:\n", substrings(USER_STR))
except ValueError as exception:
    print(f"Ошибка вода данных!\n{exception}")
