"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
print("Данная программа определяет среднее число из трёх. Приготовьтесь ввести 3 числа.")
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))
if number1 > number2 and number1 < number3:
    print(f"Среднее число: {number1}")
elif number1 > number3 and number1 < number2:
    print(f"Среднее число: {number1}")
elif number2 > number3 and number2 < number1:
    print(f"Среднее число: {number2}")
elif number2 > number1 and number2 < number3:
    print(f"Среднее число: {number2}")
elif number3 > number1 and number3 < number2:
    print(f"Среднее число: {number3}")
elif number3 > number2 and number3 < number1:
    print(f"Среднее число: {number3}")
elif number3 == number1 or number3 == number2 or number1 == number2:
    print(f"Как минимум 2 числа равны. Среднее число не определяется.")