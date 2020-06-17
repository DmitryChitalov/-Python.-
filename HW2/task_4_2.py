"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

def recur_method(i, NUM, N_COUNT, SUMM):
    if i == N_COUNT:
        print(f"Число символов равна {N_COUNT}, сумма равна {SUMM}")
    elif i < N_COUNT:
        return recur_method(i + 1, NUM / 2 * -1, N_COUNT, SUMM + NUM)

try:
    N_COUNT = int(input("ВВедите число символов: "))
    recur_method(0, 1, N_COUNT, 0)
except ValueError:
    print("Вы ввели не цифру. Повторите")