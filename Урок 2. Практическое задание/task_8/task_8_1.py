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

TIMES = int(input('How many entries do you need: '))
DIGIT = input('Which digit we are to count? ')

COUNTER = 0
for i in range(1, TIMES + 1):
    COUNTER += input(f'Entry {i}: ').count(DIGIT)
print(f'There were {COUNTER} of {DIGIT}')
