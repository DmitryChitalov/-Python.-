"""
Определение количества различных подстрок с использованием хэш-функции. 
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв. 
Требуется найти количество различных подстрок в этой строке.
"""

import hashlib


def substring_count(input_string):

    global h
    input_string = str(input_string).lower()

    length = len(input_string)

    hash_set = set()

    for i in range(length + 1):
        for j in range(i + 1, length + 1):
            print(input_string[i:j])
            h = hashlib.sha1(input_string[i:j].encode('utf-8')).hexdigest()
            hash_set.add(h)
    return len(hash_set)


some_string = input(f'Введите строку:')

print(f'Количество различных подстрок в строке {some_string}: {substring_count(some_string)}')
