"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

print('Введите длинну 3х отрезков по очереди')
side_of_triangle_a = float(input('Введите сторону а '))
side_of_triangle_b = float(input('Введите сторону b '))
side_of_triangle_c = float(input('Введите сторону c '))
if side_of_triangle_a + side_of_triangle_b <= side_of_triangle_c \
    or side_of_triangle_a + side_of_triangle_c <= side_of_triangle_b \
    or side_of_triangle_c + side_of_triangle_b <= side_of_triangle_a:
    print("С такими сторонами треугольник невозможен")
elif side_of_triangle_a == side_of_triangle_b == side_of_triangle_c:
    print('Это равносторонний треугольник')
elif side_of_triangle_a != side_of_triangle_b != side_of_triangle_c:
    print('Это разносторонний треугольник')
else:
    print('Это равнобедренный треугольник')
