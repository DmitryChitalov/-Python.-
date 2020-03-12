"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""


try:
    A = int(input("First line segment: "))
    B = int(input("Second line segment: "))
    C = int(input("Third line segment: "))

    if A + B <= C or A + C <= B or B + C <= A:
        print("Triangle doesn't exist")
    elif A != B and A != C and B != C:
        print("Scalene Triangle")
    elif A == B == C:
        print("Equilateral Triangle")
    else:
        print("Isosceles Triangle")

except ValueError:
    print('Incorrect')
