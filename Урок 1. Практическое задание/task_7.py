"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

print("Введите длины сторон предполагаемого треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    if (a == b) and (a == c) and (c == b):
        print('Треугольник равносторонний')
    else:
        if (a == b) or (b == c) or (a == c):
            print('Треугольник равнобедренный')
        else:
            print('Треугольник разносторонний')
else:
    print("Треугольник не существует")
