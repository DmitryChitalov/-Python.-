"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

try:
    A = int(input("Введите длину стороны A: "))
    B = int(input("Введите длину стороны B: "))
    C = int(input("Введите длину стороны C: "))
    if A + B <= C or A + C <= B or B + C <= A:
        print('Такого треугольника не существует')
    elif A == B == C:
        print("Треугольник равносторонний")
    elif A != B and B != C and A != C:
        print("Треугольник разносторонний")
    else:
        print('Треугольник равнобедренный')
except ValueError:
    print("Введите корректное значение")
