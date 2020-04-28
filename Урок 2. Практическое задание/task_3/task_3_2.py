"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def num_enter():
    num_user = input("Enter your number or 0 for exit: ")
    if num_user == '0':
        return
    elif num_user.isdigit():
        return int(num_user)
    else:
        print("Invalid number. Repeat entry.")
        return num_enter()


def num_reverse(num_user, num_len=0, count=1, num_rev=""):
    if num_len == 0:
        num_len = len(str(num_user))
    num_digit = (num_user % pow(10, count)) // pow(10, count - 1)
    num_rev += str(num_digit)
    if count == num_len:
        return num_rev
    return num_reverse(num_user, num_len, count + 1, num_rev)


print(num_reverse(num_enter()))

















