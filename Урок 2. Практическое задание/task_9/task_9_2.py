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

def sum_numbers(number):
    """Функция по подсчету кол-ва цифр"""
    summa = 0
    while number > 0:
        one_number = number % 10
        summa += one_number
        number = number // 10
    return summa

def recursion(count):
    number = int(input("Число : "))
    summa = sum_numbers(number)

    if count <= 1:
        return (summa, number)

    (max_sum, max_x) = recursion(count-1)

    if(summa > max_sum):
        return (summa, number)
    else:
        return (max_sum, max_x)

# start
N = int(input("Сколько будет чисел? - "))
(MAX_SUM, MAX_X) = recursion(N)
print(f"Наибольшее число по сумме цифр: ", MAX_X, "сумма его цифр:", MAX_SUM)
