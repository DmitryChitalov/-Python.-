"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

# The best practice
N = int(input('Enter N: '))
print(f'{2 / 3 * (1 - (-0.5) ** N)}')


# Strictly on task
def sum_sequence(number):
    """Counts the sum of numerical sequence"""
    result = 0
    delta = 1
    for i in range(number):
        result += delta
        delta *= -0.5
    return result


print(sum_sequence(N))
