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


def main():
    """поехали"""
    string = input('Введите строку, состоящую только из маленьких латинских букв: ')
    substrings_hash = set()
    substrings_full = set()

    for i in range(len(string)):
        for j in range(len(string), i, -1):
            sub_str = string[i:j]
            hash_str = hashlib.sha1(sub_str.encode('utf-8')).hexdigest()
            if hash_str not in substrings_hash:
                substrings_hash.add(hash_str)
                substrings_full.add(sub_str)

    print(f'Итого: {len(substrings_hash) - 1} различных подстрок в строке {string}')
    for i in substrings_full:
        print(i)


# поехали
main()
