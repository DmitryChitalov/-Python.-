"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

length_1 = int(input('Enter the length for an side of triangle 1: '))
length_2 = int(input('Enter the length for an side of triangle 2: '))
length_3 = int(input('Enter the length for an side of triangle 3: '))

if length_1 == length_2 or length_1 == length_3 or length_2 == length_3:
    if length_1 == 0 or length_2 == 0 or length_3 == 0:
        print('Looks like you entered a zero value for one of the side of the triangle')
    else:
        print('The triangle is isosceles triangle')
elif length_1 == length_2 == length_3:
    print('The triangle is equilateral triangle')
elif length_1 != length_2 != length_3:
    if length_1 == 0 or length_2 == 0 or length_3 == 0:
        print(
            'Looks like you entered a zero value for one of the '
            'side of the triangle OR you missed to enter on of the side')
    else:
        print('The triangle is versatile triangle')
