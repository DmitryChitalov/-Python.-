"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""


try:
    SIDE_A = float(input("Введите первую сторону: "))
    SIDE_B = float(input("Введите первую сторону: "))
    SIDE_C = float(input("Введите первую сторону: "))
except ValueError:
    print("Неверно введена сторона")

if (SIDE_A + SIDE_B > SIDE_C) and (SIDE_A + SIDE_C > SIDE_B) and (SIDE_C + \
    SIDE_B > SIDE_A) and SIDE_A != 0 and SIDE_B != 0 and SIDE_C != 0:
    print("Треугольник существует")
    if SIDE_A == SIDE_B == SIDE_C:
        print("Треугольник равностаронний")
    elif SIDE_A == SIDE_B or SIDE_C == SIDE_A or SIDE_B == SIDE_C:
        print("Треугольник равнобедренный")
else:
    print("Треугольник не существует")
