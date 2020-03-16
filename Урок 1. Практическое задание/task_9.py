"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""


try:
    print("Please type three numbers:")
    num_1st = int(input("First - "))
    num_2nd = int(input("Second - "))
    num_3rd = int(input("Third - "))

    if num_1st == num_2nd or num_1st == num_3rd or num_2nd == num_3rd:
        print("Some numbers are equal.")
    elif num_2nd < num_1st < num_3rd or num_2nd > num_1st > num_3rd:
        print("First number in the middle")
    elif num_1st < num_2nd < num_3rd or num_1st > num_2nd > num_3rd:
        print("Second number in the middle")
    else:
        print("Third number in the middle")
except ValueError:
    print("You entered an incorrect value.")
