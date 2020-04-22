"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).
Подсказка: можно добавить проверку, что введены равные числа
"""


number1 = int(input("number1 "))
number2 = int(input("number2 "))
number3 = int(input("number3 "))
if number1 == number2 and number1 == number3 and number2 == number3:
    print("numbers are equal")
elif number2 < number1 < number3 or number2 > number1 > number3:
    print(number1)
elif number1 > number2 > number3 or number1 < number2 < number3:
    print(number2)
else:
    print(number3)