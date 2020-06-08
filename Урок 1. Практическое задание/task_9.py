"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""


class AverageNumber:

    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def check_is_nums_different(self):
        if self.num1 != self.num2 != self.num3:
            return True
        else:
            return False

    def find_average_number(self):
        if not self.check_is_nums_different():
            return None
        if self.num1 > self.num2 and self.num1 > self.num3:
            return self.num2 if self.num2 > self.num3 else self.num3
        elif self.num2 > self.num1 and self.num2 > self.num3:
            return self.num3 if self.num3 > self.num1 else self.num1
        else:
            return self.num1 if self.num1 > self.num2 else self.num2


def main():
    try:
        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 2nd number: "))
        num3 = int(input("Enter 3rd number: "))
        av_num_instance = AverageNumber(num1, num2, num3)
        average_num = av_num_instance.find_average_number()
        if type(average_num) is not int:
            print("Error! All numbers must be different.")
            return
        print("average_num:", average_num)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
