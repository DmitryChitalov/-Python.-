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
max_s = 0
max_m = 0
NUMB_NUMB = int(input('Введите кол-во чисел: '))
for i in range(1, NUMB_NUMB+1):
    n = int(input('Введите число: '))
    m = n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    if s > max_s:
        max_s = s
        max_m = m
print('Число', max_m, 'имеет максимальную сумму цифр:', max_s)
