"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
while True:
    try:
        NUMBER = int(input('Введите количество элементов: '))
        ANSWER = 1
        TEMP_NUMBER = 1
        for i in range(NUMBER - 1):
            TEMP_NUMBER = TEMP_NUMBER / -2
            ANSWER += TEMP_NUMBER
        print(f'Количество элементов - {NUMBER}, их сумма {ANSWER}')
        break
    except ValueError:
        print(f'Ошибка ввода!')
