"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""


# Ожидает на ввод длину отрезка. Повторяет попытку ввода, пока не введено целое
def input_number(string):
    while True:
        try:
            number = input(f"Введите длину отрезка {string}\n")
            number = float(number)
            if 0 <= abs(number):
                break
            else:
                print("Введено некорректное число")
        except ValueError:
            print("Не удалось преобразовать в число")
    return number


side_a = input_number("a")
side_b = input_number("b")
side_c = input_number("c")

if side_a + side_b < side_c or side_b + side_c < side_a or side_a + side_c < side_b or side_a * side_b * side_c == 0:
    print(f"Из отрезков {side_a}, {side_b}, {side_c} невозможно составить треугольник")
elif side_a == side_b == side_c:
    print(f"Из отрезков {side_a}, {side_b}, {side_c} получится равносторонний треугольник")
elif side_a == side_b or side_b == side_c or side_a == side_c:
    print(f"Из отрезков {side_a}, {side_b}, {side_c} получится равнобедренный треугольник")
else:
    print(f"Из отрезков {side_a}, {side_b}, {side_c} получится разносторонний треугольник")
