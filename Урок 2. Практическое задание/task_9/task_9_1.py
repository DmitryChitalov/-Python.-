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

#Не законченное решение. Не хватило времени

num = int(input('How many numbers: '))
max_number = 0
sum_digits = 0

for i in range(1, num + 1):
    user_number = int(input(f"Enter your {i} number: "))
    list_digits = list(map(int, str(user_number)))
    inter_number = 0
    for _ in list_digits:
        inter_number += _
    if inter_number > max_number:
        max_number = user_number
        sum_digits = inter_number
    else:
        continue
print(f'The max number is {max_number} and the sum of it digits is {sum_digits}')


