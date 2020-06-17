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

def recur_method(NUMB, EVEN=0, ODDS=0):
    if NUMB ==0:
        return EVEN, ODDS
    else:
        CUR_N = NUMB % 10
        NUMB = NUMB // 10
        if CUR_N % 2 ==0:
            EVEN += 1
            return recur_method(NUMB, EVEN, ODDS)
        else:
            ODDS += 1
            return recur_method(NUMB, EVEN, ODDS)

try:
    NUMB = int(input("Введите натуральное число: "))
    print (f"Количество четных и нечетных цифр в числе равно: {recur_method(NUMB)}")
except ValueError:
    print("Вы ввели не цифру. Повторите")
