"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""
first_edge = input('введите первый отрезок: ')
sec_edge = input('введите второй отрезок: ')
third_edge = input('введите третий отрезок: ')

if first_edge < sec_edge + third_edge or sec_edge < first_edge + third_edge or third_edge < first_edge + sec_edge:
    if first_edge == sec_edge and sec_edge == third_edge:
        print(f'Треугольник со сторонами - равносторонний')
    elif first_edge == sec_edge or sec_edge == third_edge or third_edge == first_edge:
        print(f'Треугольник - равнобедренный')
    else:
        print(f'Треугольник - разносторонний')
else:
    print(f'Треугольника - не существует')