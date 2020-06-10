"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

print('Создаём треугольник.')
a = int(input('Задайте длинну первого отрезка: '))
b = int(input('Задайте длинну второго отрезка: '))
c = int(input('Задайте длинну третьего отрезка: '))

if a + b <= c or a + c <= b or b + c <= a:
    print('Такого треугольника небывает.')
elif a != b and a != c and b != c:
    print('Это разностороний треугольник.')
elif a == b == c:
    print('Это равностороний треугольник.')
else:
    print('Это равнобедренный треугольник.')
