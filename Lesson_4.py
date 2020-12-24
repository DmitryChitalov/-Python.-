"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import os
from hashlib import pbkdf2_hmac
from binascii import hexlify

cwd = os.getcwd()
salt = 'This is salt for URLs'

def print_url():
    result = ''
    with(open(cwd + '\\' + 'Lesson_4.txt')) as f:
        for data in f.readlines():
            url, _ = data.strip().split(' ')
            result += url + '\n'
    return result 

def check_url(p_url):
    with(open(cwd + '\\' + 'Lesson_4.txt')) as f:
        for data in f.readlines():
            if data == '' or data == '/n':
                return False
            else:    
                url, _ = data.strip().split(' ')
                if p_url == url:
                    return True
                else:
                    continue
    return False

def cach_url(p_url):
    obj = pbkdf2_hmac(hash_name='sha256',
                      password=bytes(p_url, 'utf-8'),
                      salt=bytes(salt, 'utf-8'),
                      iterations=100000)
    hash_url = hexlify(obj)
    with(open(cwd + '\\' + 'Lesson_4.txt', 'a')) as f:
        f.write(p_url + ' ' + str(hash_url) + '\n')


while True:
    print(f'These URLs have been cashed\n{print_url()}')
    inp_str = input('Plase provide new URL or press "q" for exit:').lstrip().rstrip()
    if inp_str.lower() == 'q':
        break 
    if not check_url(inp_str):
        print(f'There is no cash for URL {inp_str}')
        answer = input('Create (y/n): ').lstrip().rstrip()
        if answer.lower() == 'y':
            cach_url(inp_str)
            print(f'URL {inp_str} has been created')
            answer = input('Continue? (y/n): ').lstrip().rstrip()
            if answer.lower() == 'y':
                continue
            else:
                break
        else:
            break
    else:
        print(f'Cash for {inp_str} is already present')
        answer = input('Continue? (y/n): ').lstrip().rstrip()
        if answer.lower() == 'y':
            continue
        else:
            break