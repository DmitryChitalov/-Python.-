"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def check(num, count, result):
    """
    Реализация через рекурсию
    """
    if count > num:
        if result == num * (num + 1)/2:
            return 'Равенство верное'
    else:
        result += count
        return check(num, count + 1, result)


if __name__ == "__main__":
    RESULT = 0
    COUNT = 0
    try:
        NUM = int(input("Введите натуральное число: "))
        if NUM <= 0:
            print("Число должно быть натуральным")
        else:
            print(check(NUM, COUNT, RESULT))
    except ValueError:
        print("Ошибка ввода значения")
