"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

import sys


try:
    USER_NUMBER = int(input("Введите число: "))
except ValueError:
    print("Вы не ввели число")
    sys.exit()

TOTAL_EVEN = 0
TOTAL_NUMBER = 0


def recur_solution(user_number, total_even, total_number):
    """Решение задачи методом рекурсии"""
    if user_number == 0:
        print(f"Всего цифр в числе {total_number} из них четных {total_even}")
    else:
        if (user_number % 10) % 2 == 0:
            total_even += 1
        total_number += 1
        user_number = user_number // 10
        recur_solution(user_number, total_even, total_number)


recur_solution(USER_NUMBER, TOTAL_EVEN, TOTAL_NUMBER)
