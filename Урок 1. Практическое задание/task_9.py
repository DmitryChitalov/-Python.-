"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""


# Ожидает на ввод число. Повторяет попытку ввода, пока не введено целое
def input_number(string):
    while True:
        try:
            number = input(f"Введите {string} число\n")
            number = float(number)
            if 0 <= abs(number):
                break
            else:
                print("Введено некорректное число")
        except ValueError:
            print("Не удалось преобразовать в число")
    return number


first = input_number("первое")
second = input_number("второе")
third = input_number("третье")

if first < second < third:
    print(second)
elif second < first < third:
    print(first)
else:
    print(third)
