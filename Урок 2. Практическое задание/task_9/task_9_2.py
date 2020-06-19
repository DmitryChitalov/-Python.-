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


# Solution from teacher

def recur_method(quantity, steps, highest_numb, max_sum):
    summ = 0
    try:
        numb = input("Enter a number: ")
        for i in numb:
            summ += int(i)
        if summ > max_sum:
            max_sum = summ
            highest_numb = numb
        steps += 1
        if steps == quantity:
            return f"Highest number by summ of digits: {highest_numb}, the sum of digits: {max_sum}"
        else:
            return recur_method(quantity, steps, highest_numb, max_sum)
    except ValueError:
        print("Wrong value. Try again")


STEPS = 0
HIGHEST_NUMB = 0
MAX_SUM = 0
