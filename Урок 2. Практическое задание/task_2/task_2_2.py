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


def recursion(numb, even, uneven):
    # mathematical character
    if numb < 10:
        if numb % 2 == 0:
            even += 1
        else:
            uneven += 1
        print(f'Четные {even}   Нечетные {uneven}')
        return 0
    else:
        if (numb % 10) % 2 == 0:
            even += 1
        else:
            uneven += 1
        return recursion(numb // 10, even, uneven)


try:
    NUMB = abs(int(input('Введите натуральное число: ')))
except ValueError:
    print('Это не число.')
else:
    recursion(NUMB, 0, 0)
