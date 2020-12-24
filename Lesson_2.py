"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""

import os
from hashlib import pbkdf2_hmac
from binascii import hexlify

cwd = os.getcwd()
longin, passwd  = '', ''

def check_login(p_login):
    with(open(cwd + '\\' + 'Lesson_2.txt')) as f:
        for data in f.readlines():
            login, _ = data.strip().split(' ')
            if p_login == login:
                return True
            else:
                continue
    return False

def create_login(p_login):
    passwd = input('Plase provide password: ')
    obj = pbkdf2_hmac(hash_name='sha256',
                      password=bytes(passwd, 'utf-8'),
                      salt=bytes(login, 'utf-8'),
                      iterations=100000)
    passwd = hexlify(obj)
    with(open(cwd + '\\' + 'Lesson_2.txt', 'a')) as f:
        f.write(login + ' ' + str(passwd) + '\n')

def authent(p_login):
    p_passwd = input('Plase provide password: ')
    obj = pbkdf2_hmac(hash_name='sha256', password=bytes(p_passwd, 'utf-8'), salt=bytes(p_login, 'utf-8'), iterations=100000)
    p_passwd = hexlify(obj)
    with(open(cwd + '\\' + 'Lesson_2.txt')) as f:
        for data in f.readlines():
            login, passwd = data.strip().split(' ')
            if p_login == login and str(p_passwd) == passwd:
                return True

while True:
    login = input('Please provide your login: ').lstrip().rstrip()
    if not check_login(login):
        answer = input('You do not have login. Do you want to create it?: (y / n) ').lstrip().rstrip()
        if answer == 'y':
            login = input('Please provide a new login: ').lstrip().rstrip()
            if check_login(login):
                print(f'Login {login} is already present, please retype')
            else:
                create_login(login)
                print(f'Your Login {login} has been created successfully')
        elif answer == 'n':
            print('Bye')
            break
    else:
        if authent(login):
            print('You are successfully authenticated. Welcome!')
            break
        else:
            print('Provided password is wrong')
            answer = input('For new attempts press "y" for exit "n") ').lstrip().rstrip()
            if answer == 'y':
                continue
            else:
                break


