"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


# Ожидает на ввод число. Повторяет попытку ввода, пока не введено целое
def input_number():
    while True:
        try:
            num = input(f"Введите положительное число\n")
            num = int(num)
            if num > 0:
                break
            else:
                print('Введено некорректное число')
        except ValueError:
            print("Не удалось преобразовать в число")
    return num


# Суммирует числа, пока n больше 0
def sum_recursion(l_res, n):
    if n:
        return sum_recursion(l_res + n, n - 1)
    else:
        return l_res


number = input_number()
res = sum_recursion(0, number)
res_formula = number * (number + 1) // 2
print(f'Результат суммирования {res}, результат формулы {res_formula}')
