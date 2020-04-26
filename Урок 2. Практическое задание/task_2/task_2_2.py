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

# Словарь значений четных и нечетных цифр числа
DICT_NUMBERS = dict()
DICT_NUMBERS['четные'] = list()
DICT_NUMBERS['нечетные'] = list()


def recursion_numbers(num, even_numbers, uneven_numbers):
    if num == 0:
        return even_numbers, uneven_numbers
    else:
        unit_number = num % 10
        if unit_number % 2 == 0:
            even_numbers += 1
            if unit_number not in DICT_NUMBERS["четные"]:
                DICT_NUMBERS["четные"].append(unit_number)
        else:
            uneven_numbers += 1
            if unit_number not in DICT_NUMBERS["нечетные"]:
                DICT_NUMBERS["нечетные"].append(unit_number)
        num = num // 10
        return recursion_numbers(num, even_numbers, uneven_numbers)


while True:
    try:
        # Ожидание ввода числа
        NUMBER = int(input('Введите натуральное число:\r\n'))
        # Если введено отрицательное число генерируем обработку исключения
        if NUMBER < 0:
            raise IOError
    except (ValueError, TypeError, IOError):
        print('Ошибка ввода. Требуется ввести положительное целое число.')
    else:
        # Вызов рекурсии
        EVEN_NUMBERS, UNEVEN_NUMBERS = recursion_numbers(NUMBER, 0, 0)
        # Вывод результатов
        print(f'В числе {NUMBER}:\r\nЧетных чисел =  {EVEN_NUMBERS}\r\nНечетных чисел = {UNEVEN_NUMBERS}')
        for key, values in DICT_NUMBERS.items():
            print(f'{key}:   {values}')
        break
