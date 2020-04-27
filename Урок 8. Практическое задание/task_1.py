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


def substring_count(user_str):
    """
    функция принимает на вход строку состоящую только из маленьких латинских букв
    функция возвращает количество различных подстрок с использованием хеш-функции
    """

    user_str = input("Введите строку из маленьких латинских букв: ")
    r = set()

    N = len(user_str)
    for i in range(N):
        if i == 0:
            N = len(user_str) - 1
        else:
            N = len(user_str)
    
        for j in range(N, i, -1):
            print(user_str[i:j])
     
           
            r.add(hashlib.sha1(user_str[i:j].encode('utf-8')).hexdigest())
   
    return r


some_string = 'papa'

print(f'Колличество различных подстрок в строке {some_string} равно {len(substring_count(some_string))}')

