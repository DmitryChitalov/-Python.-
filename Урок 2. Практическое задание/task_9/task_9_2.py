"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите число: 23
Введите число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
def max_of_two(num_a, num_b):
    if num_a > num_b:
        return num_a
    else:
        return num_b


def num_sum(num, ttl):
    if num > 0:
        current_num = num % 10
        ttl = num_sum(num // 10, ttl + current_num)
    return ttl


print(f'Number with the maximum sum of numbers: '
      f'{max_of_two(num_sum((int(input("Enter number a: "))), 0), num_sum((int(input("Enter number b: "))), 0))}')
