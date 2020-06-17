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


def my_rec(num, even_num=0, odd_num=0):
    if num == 0:
        return even_num, odd_num
    else:
        el = num % 10
        num = num // 10
        if el % 2 == 0:
            even_num += 1
            return my_rec(num, even_num, odd_num)
        else:
            odd_num += 1
            return my_rec(num, even_num, odd_num)


NUMBER = int(input('Введите целое чичло: '))

print(f'Количество четный и нечётных цифр = {my_rec(NUMBER)}')
