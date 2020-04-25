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
MAX_SUMM = 0
SUMM = 0
MAX_ROW = 0
# считаем
i = 0
ROW_NUMBER = 1
while i < TOTAL:


    ROW = USER_ROW = int(input(f'Введите число {ROW_NUMBER}: '))
    ROW_NUMBER = ROW_NUMBER + 1
    ROW_LENGTH = len(str(ROW))

    k = 1
    SUMM = 0
    while k <= ROW_LENGTH:
        NUMBER = ROW % 10
        SUMM += NUMBER
        ROW = ROW // 10
        k = k + 1

    if MAX_SUMM < SUMM:
        MAX_SUMM = SUMM
        MAX_ROW = USER_ROW

    i = i + 1

# выводим ответ
print(f'Наибольшее число по сумме цифр: {MAX_ROW}, сумма его цифр: {MAX_SUMM}')
