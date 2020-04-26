"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

try:
    SEGMENTA = int(input('A = '))
    SEGMENTB = int(input('B = '))
    SEGMENTC = int(input('C = '))

    if SEGMENTA + SEGMENTB <= SEGMENTC or \
            SEGMENTA + SEGMENTC <= SEGMENTB or \
            SEGMENTB + SEGMENTC <= SEGMENTA:
        print("Треуголльник не существует")
    elif SEGMENTA == SEGMENTB == SEGMENTC:
        print("Треугольник равносторонний")
    elif SEGMENTA != SEGMENTB and SEGMENTA != SEGMENTC and SEGMENTB != SEGMENTC:
        print("Треугольник разносторонний")
    else:
        print("Треугольник равнобедренный")
except ValueError:
    print("Введите число. Попробуйте еще раз.")
