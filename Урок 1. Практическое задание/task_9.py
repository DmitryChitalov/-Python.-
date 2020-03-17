"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

from re import sub

while 1:
    START = sub(r"[\s]]", "", input("Для начала введите 1, для выхода q: "))

    if START == "q":
        break

    while 1:
        if START == "1":
            try:
                S1, S2, S3 = list(
                    map(int, sub(r"[\s]]", "", input("Введите 3 числа через зяпятую: ")).split(","))
                )
            except ValueError:
                print("Вы ввели не числа, попробуйте еще раз")
                break

            AVERAGE = S1 if S2 < S1 < S3 or S3 < S1 < S2 else S2 if S1 < S2 < S3 or S3 < S2 < S1 else S3
            print(AVERAGE)
            break
        else:
            print("Вы выбрали несущестующее действие, попробуйте снова: ")
            break

