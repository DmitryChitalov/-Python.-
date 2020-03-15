"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

number1 = int(input())
number2 = int(input())
number3 = int(input())

if number1 > number2 and number1 > number3:
    if number2 > number3:
        print(number2)
    else:
        print(number3)
elif number1 < number2 and number1 < number3:
    if number2 > number3:
        print(number3)
    else:
        print(number2)
else:
    print(number1)
