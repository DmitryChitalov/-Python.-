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


def num_enter(message):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        else:
            print("Invalid number. Repeat entry.")


num_count = num_enter("How many numbers will there be? - ")
digit = num_enter("Which digit to count? - ")
digit_count = 0

for i in range(1, num_count + 1):
    num = num_enter(f"Number {i}: ")
    num_len = len(str(num))
    for j in range(0, num_len):
        num_dig = (num // pow(10, j)) % 10
        if num_dig == digit:
            digit_count += 1

print(f"Number {digit} occurs {digit_count} times.")





