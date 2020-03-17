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

NUMBERUSER = int(input("Сколько будет чисел?"))
NUMBERUSER1 = input("Какую цифру считать?")
SISTEMCOUNT = 0
NUMBERCOUNT = 0
while SISTEMCOUNT < NUMBERUSER:
    NUMBERUSERI = input("Введите число--")
    NUMBERCOUNT += NUMBERUSERI.count(NUMBERUSER1)
    SISTEMCOUNT += 1
print(f'Было введено {NUMBERCOUNT} цифр {NUMBERUSER1}')
