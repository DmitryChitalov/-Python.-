"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите число: 23
Введите число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def num_enter(message):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        else:
            print("Invalid number. Repeat entry.")


def check_num(num, count=-1, num_sum=0):
    if count == 0:
        return num_sum
    if count == -1:
        count = len(str(num))
    num_sum += (num // pow(10, count-1)) % 10
    return check_num(num, count - 1, num_sum)


def sum_max(num_count, count=1, max_sum=0):
    if num_count + 1 == count:
        return
    num = num_enter(f"Number {count}: ")
    num_sum = check_num(num)
    global MAX_NUM
    global MAX_SUM
    if num_sum > MAX_SUM:
        MAX_SUM = num_sum
        MAX_NUM = num
    return sum_max(num_count, count + 1, max_sum)


NUM_COUNT = num_enter("How many numbers will there be? - ")
MAX_SUM = 0
MAX_NUM = 0

sum_max(NUM_COUNT)
print(f"The largest number by the sum of digits: {MAX_NUM}, the sum of its digits: {MAX_SUM}.")
