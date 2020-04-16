"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""


def triangle():
    print("Please type three line lengths:")
    len_1st = int(input("First - "))
    len_2nd = int(input("Second - "))
    len_3rd = int(input("Third - "))

    if (len_1st + len_2nd > len_3rd) \
            and (len_1st + len_3rd > len_2nd) \
            and (len_2nd + len_3rd > len_1st):
        print("Such a triangle exists")
        if len_1st == len_2nd == len_3rd:
            print("Triangle is equilateral.")
        elif (len_1st == len_2nd and len_1st != len_3rd) or \
                (len_1st == len_3rd and len_1st != len_2nd) or\
                (len_3rd == len_2nd and len_1st != len_3rd):
            print("Triangle is isosceles.")
        else:
            print("Triangle with different sides.")
    else:
        print("Such a triangle doesn't exists")


try:
    triangle()
except ValueError:
    print("You entered an incorrect value.")
