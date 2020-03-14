"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

SIDE_1 = int(input('Введите длинну первоно отрезка: '))
SIDE_2 = int(input('Введите длинну второго отрезка: '))
SIDE_3 = int(input('Введите длинну третьего отрезка: '))

MAX_SIDE = SIDE_1
if MAX_SIDE < SIDE_2:
    MAX_SIDE = SIDE_2
if MAX_SIDE < SIDE_3:
    MAX_SIDE = SIDE_3

if MAX_SIDE == SIDE_1 + SIDE_2 + SIDE_3 - MAX_SIDE:
    print(f"Из отрезков длинной {SIDE_1}, {SIDE_2} и {SIDE_3} построить треугольник нельзя.")
elif SIDE_1 == SIDE_2 and SIDE_2 == SIDE_3:
    print("Из отрезков равной длинны получится равносторонний треугольник")
elif SIDE_1 == SIDE_2 or SIDE_2 == SIDE_3 or SIDE_3 == SIDE_1:
    print(f'Из введеных вами отрезков получчится равнобедренный треугольник')
else:
    print('Из введены вами отрезков получится ни чем не пиримичательный треугольник')
