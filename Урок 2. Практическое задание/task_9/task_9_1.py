"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите очередное число: 23
Введите очередное число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ

К сожалению, не смог найти правила по переносу содерживого
фигурных скобок в f строке. В связи с этим превышение лимита
по длине символов на 23 строке.
"""
def max_of_two(num_a, num_b):
    if num_a > num_b:
        return num_a
    else:
        return num_b


def num_sum(num):
    ttl_summ = 0
    while num > 0:
        current_num = num % 10
        ttl_summ += current_num
        num = num // 10
    return ttl_summ


print(f'Number with the maximum sum of numbers: '
      f'{max_of_two((num_sum(int(input("Enter number a: ")))),(num_sum(int(input("Enter number b: ")))))}')
