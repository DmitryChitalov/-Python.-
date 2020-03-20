"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
"""
NUM = int(input('Введите любое натуральное число: '))
COUNTER = NUM
RIGHT_SIDE = (NUM * (NUM + 1)) // 2
LEFT_SIDE = 0
while COUNTER > 0:
    LEFT_SIDE += COUNTER
    COUNTER -= 1
RESULT = LEFT_SIDE == RIGHT_SIDE
print(
    f'Равенство 1+2+...+n = n(n+1)/2 выполняется с результатом {RESULT}, '
    f'так как левая часть равенства равна {LEFT_SIDE}, правая равна {RIGHT_SIDE}, при n = {NUM}')
