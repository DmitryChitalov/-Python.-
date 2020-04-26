"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
Для извлечения цифр числа используйте арифм. операции
Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных
ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

# Словарь значений четных и нечетных цифр числа
DICT_NUMBERS = dict()
DICT_NUMBERS['четные'] = list()
DICT_NUMBERS['нечетные'] = list()
while True:
    try:
        NUMBER = int(input('Введите натуральное число:\r\n'))
        # Если введено отрицательное число генерируем обработку исключения
        if NUMBER < 0:
            raise IOError
    except (ValueError, TypeError, IOError):
        print('Ошибка ввода. Требуется ввести положительное целое число.')
    else:
        EVEN_NUMBERS = 0
        UNEVEN_NUMBERS = 0
        NUM = NUMBER
        while NUM > 0:
            UNIT_NUMBER = NUM % 10
            if UNIT_NUMBER % 2 == 0:
                EVEN_NUMBERS += 1
                if UNIT_NUMBER not in DICT_NUMBERS["четные"]:
                    DICT_NUMBERS["четные"].append(UNIT_NUMBER)
            else:
                UNEVEN_NUMBERS += 1
                if UNIT_NUMBER not in DICT_NUMBERS["нечетные"]:
                    DICT_NUMBERS["нечетные"].append(UNIT_NUMBER)
            NUM = NUM // 10
        print(f'В числе {NUMBER}:\r\nЧетных чисел =  {EVEN_NUMBERS}\r\nНечетных чисел = {UNEVEN_NUMBERS}')
        for key, values in DICT_NUMBERS.items():
            print(f'{key}:   {values}')
        break
