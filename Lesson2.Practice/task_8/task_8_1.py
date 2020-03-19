"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def count_digit():
    """
    Реализация через цикл
    """
    curr_count = 0
    need_nums_count = 0
    try:
        count_nums = int(input("Введите количество вводимых чисел: "))
        if count_nums <= 0:
            return f'Число должно быть положительным'
        digit = int(input("Введите цифру, которую будем считать: "))
        if digit < 0 or digit > 10:
            return f'Задайте цифру от 0 до 9'
        while curr_count < count_nums:
            num = int(input("Введите число: "))
            while num > 0:
                if num % 10 == digit:
                    need_nums_count += 1
                num //= 10
            curr_count += 1
        return f'Было введено {nums_count} цифр {digit}'
    except ValueError:
        print("Ошибка ввода значения")


if __name__ == "__main__":
    print(count_digit())
