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


def num_enter(message):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        else:
            print("Invalid number. Repeat entry.")


num_count = num_enter("How many numbers will there be? - ")
max_num = 0
max_sum = 0

for i in range(1, num_count + 1):
    num = num_enter(f"Number {i}: ")
    num_len = len(str(num))
    num_sum = 0
    for j in range(0, num_len):
        num_dig = (num // pow(10, j)) % 10
        num_sum += num_dig
    if num_sum > max_sum:
        max_num = num
        max_sum = num_sum

print(f"The largest number by the sum of digits: {max_num}, the sum of its digits: {max_sum}.")
