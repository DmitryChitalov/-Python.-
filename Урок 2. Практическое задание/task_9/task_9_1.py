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
# чего считаем
TOTAL = int(input('Введите сколько будет чисел: \n'))
max_summ = 0
summ = 0
max_row = 0
# считаем
i = 0
ROW_NUMBER = 1
while i < TOTAL:


    ROW = user_row = int(input(f'Введите число {ROW_NUMBER}: '))
    ROW_NUMBER = ROW_NUMBER + 1
    ROW_LENGTH = len(str(ROW))

    k = 1
    summ = 0
    while k <= ROW_LENGTH:
        NUMBER = ROW % 10
        summ += NUMBER
        ROW = ROW // 10
        k = k + 1

    if max_summ < summ:
        max_summ = summ
        max_row = user_row

    i = i + 1

# выводим ответ
print(f'Наибольшее число по сумме цифр: {max_row}, сумма его цифр: {max_summ}')