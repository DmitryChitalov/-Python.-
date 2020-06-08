"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""


class WrongTriangleError(Exception):
    def __init__(self, error_msg, *args, **kwargs):
        self.error_message = error_msg

    def __str__(self):
        return self.error_message

    def __repr__(self):
        return self.error_message


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle_valid(self):

        if (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.b + self.c <= self.a):
            return False
        else:
            return True

    def get_triangle_type(self):
        try:
            if not self.is_triangle_valid():
                raise WrongTriangleError("Wrong triangle side sizes.")
            if self.a == self.b == self.c:
                result = "Equilateral triangle (равносторонний)"
            elif self.a != self.b != self.c:
                result = "Versatile triangle (разносторонний)"
            else:
                result = "Isosceles triangle (равнобедренный)"
        except WrongTriangleError as we:
            result = we
        except Exception as ex:
            result = ex
        return result


def main():
    try:
        a = abs(int(input("Enter triangle 1st side size: ")))
        b = abs(int(input("Enter triangle 2nd side size: ")))
        c = abs(int(input("Enter triangle 3rd side size: ")))
        triangle = Triangle(a, b, c)
        triangle_type = triangle.get_triangle_type()
        print(triangle_type)
    except ValueError:
        print("Error! Only integer numbers must be entered.")


if __name__ == '__main__':
    main()
