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


def unique_substring(user_str: str) -> int:
    """
    Подсчёт количества уникальных подстрок.
    Алгоритм имеет сложность O(n**2)
    """
    ss_set = set()
    len_str = len(user_str)
    for cursor in range(len_str):
        for shift in range(1, len_str - cursor + 1):
            substring = user_str[cursor: cursor + shift]
            if substring == user_str:
                pass
            else:
                ss_set.add(hashlib.sha1(substring.encode()).hexdigest())
    del len_str
    return len(ss_set)


if __name__ == "__main__":

    USER_STRING = input('Введите строку: ')
    print(
        'Количество уникальных подстрок в данной строке =',
        unique_substring(USER_STRING)
    )
