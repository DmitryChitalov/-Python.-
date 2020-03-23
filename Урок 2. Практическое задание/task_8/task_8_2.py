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

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

def count_number(search_number, number):
    """Функция по подсчету кол-ва цифр"""
    count = 0
    while number > 0:
        one_number = number % 10
        if one_number == search_number:
            count = count + 1
        number = number // 10
    return count

def recursion(count, search_number):
    """Рекурсия решения фцнкции"""
    if count == 0:
        return 0
    number = int(input("Число " + str(count) + ": "))
    result = count_number(search_number, number)
    return result + recursion(count - 1, search_number)

N = int(input("Сколько будет чисел? - "))
O = int(input("Какую цифру считать? - "))
SUM = recursion(N, O)

print(f"Было введено", SUM, "цифр '", O, "'")