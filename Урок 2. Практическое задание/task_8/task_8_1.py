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

NUMBERS_QUANTITY = int(input("Сколько будет чисел? - "))
DIGIT_FOR_COUNT = int(input("Какую цифру считать? - "))
DIGIT_COUNT = 0
NUMBER_FOR_COUNT = "0"

for I in range(NUMBERS_QUANTITY):
    INVITE_FOR_NUMBER = "Число " + str(I + 1) + ": "
    NUMBER_FOR_COUNT += input(INVITE_FOR_NUMBER)

I = 0
N_F_C = len(NUMBER_FOR_COUNT)
NUMBER_FOR_COUNT = int(NUMBER_FOR_COUNT)

while I <= N_F_C:
    if (NUMBER_FOR_COUNT % 10) == DIGIT_FOR_COUNT:
        DIGIT_COUNT += 1
    NUMBER_FOR_COUNT = NUMBER_FOR_COUNT // 10
    I += 1

print("Было введено " + str(DIGIT_COUNT) + " цифр '" + str(DIGIT_FOR_COUNT) + "'")
