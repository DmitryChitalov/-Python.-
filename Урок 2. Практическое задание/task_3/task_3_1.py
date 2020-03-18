"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
Используйте арифм операции для формирования числа, обратного введенному

Пример:
Введите число: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

while True:
    break_point = False
    while True:
        num_user = input("Enter your number or 0 for exit: ")
        if num_user == '0':
            break_point = True
            break
        elif num_user.isdigit():
            break
        else:
            print("Invalid number. Repeat entry.")
    if break_point:
        break
    num_len = len(num_user)
    num_user = int(num_user)
    num_reverse = ""

    for i in range(1, num_len + 1):
        num_digit = (num_user % pow(10, i)) // pow(10, i - 1)
        num_reverse += str(num_digit)
    num_reverse = int(num_reverse)
    print(f"Reverse number: {num_reverse}")
