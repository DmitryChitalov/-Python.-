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


def cnt_subst(l_string):
    hashes = dict()

    # В двойном цикле получаем все возможные подстроки
    for i in range(len(l_string)):
        for j in range(i+1, len(l_string)+1):
            # Само слово не учитываем
            if j - i == len(l_string):
                continue
            subst = l_string[i:j]
            # Хэш строки
            hash = hashlib.md5(subst.encode()).hexdigest()
            hashes[hash] = subst
    # Вывод всех подстрок
    for i in hashes:
        print(hashes[i])
    return len(hashes)


string = input('Введите строку: ')
print(cnt_subst(string))
