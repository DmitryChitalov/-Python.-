"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
def equality(N, NUMBER_1):
    try:
        if int(N) > 0:
            NUMBER_2 = int(N) * (int(N) + 1) // 2
            if NUMBER_1 != NUMBER_2:
                for el in range(1, int(N) + 1):
                    NUMBER_1 += el
                    return equality(N, NUMBER_1)
            else:
                return f'Равенство выполняется: {NUMBER_1} = {NUMBER_2}'
        else:
            return 'Некоректное значение. Введите натуральное число.'
    except ValueError:
        print('Некоректное значение. Введите натуральное число.')

N = input("Введите число n : ")
print(equality(N, NUMBER_1=0))
