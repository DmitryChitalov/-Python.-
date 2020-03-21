"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


# Ожидает на ввод число. Повторяет попытку ввода, пока не введено целое
def input_number(string):
    while True:
        try:
            num = input(f"{string}\n")
            num = int(num)
            break
        except ValueError:
            print("Не удалось преобразовать в число")
    return num


# Ожидает на ввод число. Повторяет попытку ввода, пока не введено целое
def input_digit():
    while True:
        try:
            num = input(f"Введите цифру\n")
            num = int(num)
            if 0 <= num <= 9:
                break
            else:
                print('Введено некорректное число')
        except ValueError:
            print("Не удалось преобразовать в число")
    return num


# Считаем количество определенных цифр в числе
def count_digits(l_number, l_digit):
    tmp_number = abs(l_number)
    l_count = 1 if tmp_number % 10 == l_digit else 0
    if tmp_number < 10:
        return l_count
    else:
        l_count += count_digits(tmp_number // 10, l_digit)
    return l_count


# Считывает последовательность и считает количество определенных цифр
def check_sequence(l_count, l_count_digit, l_digit):
    if l_count > 0:
        number = input_number('Введите очередное число')
        l_count_digit += count_digits(number, l_digit)
        return check_sequence(l_count - 1, l_count_digit, l_digit)
    else:
        return l_count_digit


count = input_number('Сколько будет чисел?')
digit = input_digit()
count_digit = check_sequence(count, 0, digit)
print(f'В последовательности чисел "{digit}" встретилась {count_digit} раз')
