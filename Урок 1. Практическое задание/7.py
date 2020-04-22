#!/usr/local/bin/python3

"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

tr_side_1 = int(input("Длинам отрезка 1"))
tr_side_2 = int(input("Длинам отрезка 2"))
tr_side_3 = int(input("Длинам отрезка 3"))
if tr_side_1 + tr_side_2 > tr_side_3 and tr_side_1 + \
        tr_side_3 > tr_side_2 and tr_side_2 + tr_side_3 > tr_side_1:
    if tr_side_1 == tr_side_2 or tr_side_2 == tr_side_3 or tr_side_1 == tr_side_3:
        print('равнобедренным')
    elif tr_side_1 != tr_side_2 and tr_side_2 != tr_side_3:
        print('разносторонним')
    else:
        print('равносторонним')
else:
    print("Треугольник не существует")
