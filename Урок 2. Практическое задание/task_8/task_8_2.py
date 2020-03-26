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


def num_enter(message):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        else:
            print("Invalid number. Repeat entry.")


def check_num(num, digit, count=-1, digit_count=0):
    if count == 0:
        return digit_count
    if count == -1:
        count = len(str(num))
    num_dig = (num // pow(10, count-1)) % 10
    if num_dig == digit:
        digit_count += 1
    return check_num(num, digit, count - 1, digit_count)


def dig_count(num_count, digit, count=1, digit_count=0):
    if num_count + 1 == count:
        return digit_count
    num = num_enter(f"Number {count}: ")
    digit_count += check_num(num, digit)
    return dig_count(num_count, digit, count + 1, digit_count)


NUM_COUNT = num_enter("How many numbers will there be? - ")
DIGIT = num_enter("Which digit to count? - ")
DIGIT_COUNT = dig_count(NUM_COUNT, DIGIT)

print(f"Number {DIGIT} occurs {DIGIT_COUNT} times.")
