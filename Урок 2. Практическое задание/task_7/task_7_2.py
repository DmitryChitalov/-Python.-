"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
def equation_checker(num, ttl_sum, num_copy):
    num_copy = num_copy
    if num > 0:
        ttl_sum += num
        equation_checker(num - 1, ttl_sum, num_copy)
    else:
        if ttl_sum == num_copy * (num_copy + 1) // 2:
            return print(f'Equation is true: {ttl_sum} = '
                         f'{num_copy} * ({num_copy} + 1) // 2')


ttl_sum = 0
user_num = int(input('Enter the number: '))
equation_checker(user_num, ttl_sum, user_num)
