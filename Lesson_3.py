"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
import hashlib

inp_str = input('Please provide any string contains only English letters:')
s = set() 
n = len(inp_str)

for i in range(0, n+1):
    for j in range(0, n+1):
        h_inp_str = hashlib.sha256(bytes(inp_str, 'utf-8')).hexdigest()
        h_substr = hashlib.sha256(bytes(inp_str[i : j], 'utf-8')).hexdigest()
        if h_substr == h_inp_str or inp_str[i:j] == '':
            continue    
        else:
            s.add(inp_str[i:j])
print(s) 