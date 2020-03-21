"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
def find_numbers(NUMBER, count):
    try:
        if int(NUMBER) > 0:
            if count != int(NUMBER):
                k, summ = 1., 0.
                for el in range(int(NUMBER)):
                    summ += k
                    k /= -2
                return summ
            return find_numbers(int(NUMBER), count +1)
        raise ValueError
    except ValueError:
        return 'Некорректное значение. Введите натуральное число.'

NUMBER = input('Введите натуральное число : ')
print(find_numbers(NUMBER, count=0))
