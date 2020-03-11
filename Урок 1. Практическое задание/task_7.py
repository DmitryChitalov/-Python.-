"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

try:
    LENGTH_1 = float(input("Введите длину первого отрезка\n"))
    LENGTH_2 = float(input("Введите длину второго отрезка\n"))
    LENGTH_3 = float(input("Введите длину третьего отрезка\n"))

    if LENGTH_1 <= 0 or LENGTH_2 <= 0 or LENGTH_3 <= 0:
        print("Длины не могут быть отрицательными")
    elif LENGTH_1 + LENGTH_2 > LENGTH_3 and \
            LENGTH_2 + LENGTH_3 > LENGTH_1 and LENGTH_1 + LENGTH_3 > LENGTH_2:
        print(
            f"Треугольник со сторонами {LENGTH_1} , {LENGTH_2} , {LENGTH_3} существует\n")
        if LENGTH_1 == LENGTH_2 and LENGTH_1 == LENGTH_3:
            print("Треугольник равносторонний")
        elif LENGTH_1 == LENGTH_2 or LENGTH_1 == LENGTH_3 or LENGTH_2 == LENGTH_3:
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")
    else:
        print("Треугольник с заданными сторонами не существует")
except ValueError:
    print("Нужно ввести число")
