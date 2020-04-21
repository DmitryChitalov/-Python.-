"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Such triangle does not exist")
elif a != b and a != c and b != c:
    print("It is a miscellaneous triangle")
elif a == b == c:
    print("It is a equilateral triangle ")
else:
    print("It is a isosceles triangle")
