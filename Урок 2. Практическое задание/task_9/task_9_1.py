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
try:
    N = int(input("Введите количество чисел:  "))
    MAX_NUMBER = 0
    MAX_SUM = 0
    for i in range(1, N+1):
        NUMBER = int(input(f"Число {i}: "))
        M = NUMBER
        SUM = 0
        while M > 0:
            SUM += M % 10
            M //= 10
        if MAX_SUM < SUM:
            MAX_SUM = SUM
            MAX_NUMBER = NUMBER
    print(f"Наибольшее число по сумме цифр: {MAX_NUMBER}, сумма его цифр: {MAX_SUM}.")
except ValueError:
    print("Неправильный ввод данных.")
