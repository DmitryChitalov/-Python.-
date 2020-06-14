"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
from random import randint

user_count = int(input('Сколько будет чисел? - '))
search_num = int(input('Какую цифру считать? - '))
COUNT_NUM = 0

for idx in range(1, user_count + 1):
    current_num = randint(1, 1000)
    print(f'Число {idx}: {current_num}')
    for num in str(current_num):
        COUNT_NUM += 1 if int(num) == search_num else 0

print(f"Было введено {COUNT_NUM} цифр '{search_num}'")
