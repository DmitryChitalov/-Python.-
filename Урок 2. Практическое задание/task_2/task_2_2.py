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

NUM = int(input("ВВедите натуральное число: "))

def odd_even(num, odd=0, even=0):
    """Посчитать четные и нечетные цифры введенного натурального числа"""
    if (num % 10) % 2 == 0:
        even += 1
    else:
        odd += 1
    if len(str(num)) == 1:
        print(f"Количество четных и нечетных цифр в числе равно: ({even}, {odd})")
    else:
        odd_even(num // 10, odd, even)

odd_even(NUM)
