"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

def sum_row(count_iter, num=1, sum=0):
    if count_iter == 0:
        print(f'Сумма элементов ряда: {sum}')
        return
    sum = sum + num
    num /= -2
    count_iter -= 1
    sum_row(count_iter, num, sum)

try:
    COUNT_ITER = int(input('Введите количество элементов из ряда: '))
    sum_row(COUNT_ITER)
except ValueError:
    print('Необходимо вводить число.')
