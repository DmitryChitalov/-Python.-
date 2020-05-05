"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

PARAM_1 = int(input("Введите первую длину: "))
PARAM_2 = int(input("Введите вторую длину: "))
PARAM_3 = int(input("Введите третью длину: "))
if PARAM_1 + PARAM_2 <= PARAM_3 or PARAM_1 + PARAM_3 <= PARAM_2 or PARAM_3 + PARAM_2 <= PARAM_1:
    print("Треугольник не существует")
else:
    if PARAM_1 != PARAM_2 and PARAM_1 != PARAM_3 and PARAM_2 != PARAM_3:
        print("Треугольник разносторонний")
    else:
        if PARAM_1 == PARAM_2 == PARAM_3:
            print("Треугольник равносторонний")
        else:
            print("Равнобедренный")