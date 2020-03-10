"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""
while True:
    try:
        print('Данная программа по трем отрезкам определит существует ли треугольник или нет')
        LEG1 = int(input("a = "))
        LEG2 = int(input("b = "))
        LEG3 = int(input("c = "))
        if LEG1 + LEG2 <= LEG3 or LEG1 + LEG3 <= LEG2 or LEG2 + LEG3 <= LEG1:
            print("Треугольник не существует")
        elif LEG1 != LEG2 and LEG1 != LEG3 and LEG2 != LEG3:
            print("Разносторонний")
        elif LEG1 == LEG2 == LEG3:
            print("Равносторонний")
        else:
            print("Равнобедренный")
        break
    except ValueError:
        print(f'Ошибка ввода')