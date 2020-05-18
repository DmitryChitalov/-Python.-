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
import collections


def hash_count(word):
    list_hash = {}

    word = str(word)
    word_hash = hashlib.sha1(bytes(word, 'utf-8')).hexdigest()
    collections.OrderedDict(list_hash)
    for i in range(len(word)):
        letter = ''
        for j in word[i:]:
            letter += j
            hash_letter = hashlib.sha1(bytes(letter, 'utf-8')).hexdigest()
            if hash_letter != word_hash and hash_letter not in list_hash:
                list_hash[letter] = hash_letter
    return list_hash


while (1):
    user_input = input('Введите строку из маленьких латинских букв: ')
    user_input = user_input.lower()
    if user_input == '':
        print('Строка пуста, попробуйте еще раз!')
    else:
        hash_user_input = hash_count(user_input)
        print(f'\nВ строке \033[33m{user_input}\033[0m содержится различных подстрок: {len(hash_user_input)}')

        for key, value in hash_user_input.items():
            print('\t', f'{key} - {value}')

        break



