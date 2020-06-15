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


# Не законченное решение. Не хватило времени

# num = int(input('How many numbers: '))
# max_number = 0
# sum_digits = 0
#
# for i in range(1, num + 1):
#     user_number = int(input(f"Enter your {i} number: "))
#     list_digits = list(map(int, str(user_number)))
#     inter_number = 0
#     for _ in list_digits:
#         inter_number += _
#     if inter_number > max_number:
#         max_number = user_number
#         sum_digits = inter_number
#     else:
#         continue
# print(f'The max number is {max_number} and the sum of it digits is {sum_digits}')


# Solution from teacher

def cycle_method(quant):
    steps = 0
    max_sum = 0

    for _ in range(0, quant):
        try:
            numb = input("Entere the next number: ")
            summ = 0
            for i in numb:
                summ += int(i)
            if summ > max_sum:
                max_sum = summ
                highest_numb = numb
            steps += 1
        except ValueError:
            print("Wrong value. Try again")
    return f"Highest munber by summ of digits: {highest_numb}, the sum of digits: {max_sum}"


try:
    QUANT = int(input("Enter number of digits: "))
    print(cycle_method(QUANT))
except ValueError:
    print("Wrong value. Try again")
