"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите очередное число: 23
Введите очередное число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
def user_number():
    user_num = int(input('Введите количество чисел: '))

    def sum_number(user_num, max_s_n=0, m_number=0):
        if user_num == 0:
            return print(f'Максимальная сумма введенных чисел {max_s_n}, '
                         f'это число {m_number}')

        user_in = int(input('Введите число: '))
        max_number = user_in
        max_sum = 0
        while user_in > 0:
            max_sum += user_in % 10
            user_in //= 10
            if max_sum > max_s_n:
                max_s_n = max_sum
                m_number = max_number
        user_num -= 1
        return sum_number(user_num, max_s_n, m_number)

    sum_number(user_num)


user_number()