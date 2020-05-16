import hashlib

str = input('Введите строку: ')

substring = {}

def func(str):
    for i in range(len(str) - 1):
        for n in range(1, len(str) + 1):
            if i < n and str[i:n] != str:
                hash= hashlib.md5(str[i:n].encode())
                substring.update({hash.hexdigest(): str[i:n]})
    return substring

id = 1
for i in func(str).values():
    print(f"{id}: {i}")
    id+=1
print(f'Всего строк: {len(substring)}')