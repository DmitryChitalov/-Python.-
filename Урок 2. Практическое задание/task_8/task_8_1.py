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


def count_digits(l_number, l_digit):
    tmp_number = abs(l_number)
    l_count = 0
    if l_number == 0 and l_digit == 0:
        l_count = 1
    while tmp_number:
        tmp_digit = tmp_number % 10
        if tmp_digit == l_digit:
            l_count += 1
        tmp_number //= 10
    return l_count


count = input_number('Сколько будет чисел?')
digit = input_digit()
count_digit = 0
while count:
    number = input_number('Введите число')
    count_digit += count_digits(number, digit)
    count -= 1
print(f'В последовательности чисел "{digit}" встретилась {count_digit} раз')
