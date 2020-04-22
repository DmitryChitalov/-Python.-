''' task_1'''

USER_NUM = int(input('Введите трехзначное число: '))

DIG1 = USER_NUM // 100
DIG2 = (USER_NUM // 10) % 10
DIG3 = (USER_NUM % 10)

print(DIG1 + DIG2 + DIG3)
print(DIG1 * DIG2 * DIG3)

''' task_2'''

x = 5
y = 6

print(x & y)
print(x | y)
print(x ^ y)
print(~ x)
print(x >> 2)
print(x << 2)

''' task_3'''

X1 = int(input('Введите значение координаты Х первой точки'))
Y1 = int(input('Введите значение координаты У первой точки'))
X2 = int(input('Введите значение координаты Х второй точки'))
Y2 = int(input('Введите значение координаты У второй точки'))

k = (Y1 - Y2) // (X1 - X2)
b = Y1 - X1 * k

print("y = ", k, "x +" , b)

''' task_4'''

from random import random

MAX_NUM = int(input('Максимальная граница: '))
MIN_NUM = int(input('Минимальная граница: '))

NUMB = int(random() * (MAX_NUM - MIN_NUM)) + MIN_NUM
print(NUMB)

MUX_NUM = float(input('Максимальная граница: '))
MIN_NUM = float(input('Минимальная граница: '))

NUMB = random() * (MAX_NUM - MIN_NUM) + MIN_NUM
print(NUMB)


import string

LETTER1 = str(input('Первая буква: '))
LETTER2 = str(input('Вторая буква: '))

LETTER = random.choice(string.ascii_lowercase) #не понимаю как задать диапазон для букв
print(LETTER)


''' task_5'''

LETTER1 = str(input('Введите первую букву: '))
LETTER2 = str(input('Введите вторую букву: '))

print('Буква', LETTER1, 'стоит на месте', ord(LETTER1) - 96, ', буква', LETTER2, 'стоит на месте', ord(LETTER2) - 96)

if ord(LETTER2) > ord(LETTER1):
    DIFF = ord(LETTER2) - ord(LETTER1)
else:
    DIFF = ord(LETTER1) - ord(LETTER2)

print('Между ними столько букв: ', DIFF)


''' task_6'''

LETTER_NUM = int(input('Введите номер буквы: '))
print('Введёному номеру соответствует буква: ', chr(LETTER_NUM + 96))

''' task_7'''

a = int(input('Длина одной стороны треугольника: '))
b = int(input('Длина второй стороны треугольника: '))
c = int(input('Длина третьей стороны треугольника'))

if a >= b and a >= c and (b + c) > a:
    if a == b or a == c or b == c:
        print('Треугольник равнобедренный')
    elif a == b and a == c:
        print('Треугольник равносторонний')
    else:
        print('Треугольник разносторонний')
elif b >= a and b >= c and (a + c) > b:
    if a == b or a == c or b == c:
        print('Треугольник равнобедренный')
    elif a == b and a == c:
        print('Треугольник равносторонний')
    else:
        print('Треугольник разносторонний')
elif c >= a and c >= b and (a + b) > c:
    if a == b or a == c or b == c:
        print('Треугольник равнобедренный')
    elif a == b and a == c:
        print('Треугольник равносторонний')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольника не существует')

''' task_8'''

# Обычное ветвление
YEAR = int(input('Введите год: '))

if YEAR % 4 == 0 and YEAR % 100 != 0:
    print('Високосный год')
elif YEAR % 400 == 0:
    print('Високосный год')
else:
    print('Это невисокосный год')

# Тернарный оператор

YEAR = int(input('Введите год: '))

YEAR_TYPE = 'Високосный год' if YEAR % 4 == 0 and YEAR % 100 != 0 or YEAR % 400 == 0 else 'Это невисокосный год'
print(YEAR_TYPE)

''' task_9'''

NUM_A = int(input('Введите первое число: '))
NUM_B = int(input('Введите второе число: '))
NUM_C = int(input('Введите третье число: '))

if NUM_A > NUM_B and NUM_A > NUM_C:
    if NUM_B > NUM_C:
        print(NUM_B)
    else:
        print(NUM_C)
elif NUM_A < NUM_B and NUM_B < NUM_C:
    print(NUM_B)
elif NUM_A < NUM_C and NUM_C < NUM_B:
    print(NUM_C)
else:
    print(NUM_A)



