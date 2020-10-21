"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
user_num = int(input('Enter the number: '))
user_num_copy = user_num
ttl_sum = 0
base_equation = user_num * (user_num + 1) // 2

while user_num != 0:
    ttl_sum += user_num
    user_num -= 1
if ttl_sum == base_equation:
    print(f'Equation is true: {ttl_sum} = {user_num_copy} * ({user_num_copy} + 1) // 2')
