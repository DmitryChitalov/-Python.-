"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите очередное число: 23
Введите очередное число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

NUMBERUSER = int(input("Сколько будет чисел?"))
SISTEMCOUNT = 0
NUMBERCOUNT = 0
DIVIDERNUM = 0
ASER = 0
LOTNUMBER = 0
WHATNUMBER = 0
while SISTEMCOUNT < NUMBERUSER:
    NUMBERUSERINPUT = str(input("Введите очередное число: ?"))
    SISTEMCOUNT += 1
    for i in str(NUMBERUSERINPUT):
        NUMBERCOUNT += int(NUMBERUSERINPUT[ASER])
        ASER += 1
    if NUMBERCOUNT >= DIVIDERNUM:
        DIVIDERNUM = NUMBERCOUNT
        LOTNUMBER = NUMBERUSERINPUT
        WHATNUMBER += 1
    ASER = 0
    NUMBERCOUNT = 0
print(f'Cумма цифра равна {DIVIDERNUM} у числа {LOTNUMBER} и оно большее из введеных')