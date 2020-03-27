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
def fun(a, steps, high, max):
    sum = 0
    try:
        number = input("Введите число: ")
        for i in number:
            sum += int(i)
        if sum > max:
            max = sum
            high = number
        steps += 1
        if steps == a:
            return f"Наибольшее число по сумме цифр: {high}, сумма его цифр: {max}"
        else:
            return fun(a, steps, high, max)
    except ValueError:
        print("Вы ввели некорректные данные")

STEPS = 0
HIGH = 0
MAX = 0

try:
    A = int(input("Введите количество чисел: "))
    print(fun(A, STEPS, HIGH, MAX))
except ValueError:
    print("Вы ввели некорректные данные")
