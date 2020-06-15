"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


#Solution 1
# n = int(input('Enter how many elements to sum:'))
# digit = 1
# summary = 0
#
# while n > 0:
#     summary += digit
#     digit /= -2
#     n -= 1
# print(summary)


#Solution 2
# n = int(input('Enter how many elements to sum:'))
# sum_ = 1 * (1 - (-0.5)**n) / (1 - (-0.5))
# print(sum_)


# Solution from teacher

def cycle_method(n_count):
    numb = 1
    i = 0
    common_sum = 0
    while i < n_count:
        common_sum += numb
        numb = numb / 2 * -1
        i += 1
    return common_sum

try:
    N_COUNT = int(input("Enter number of elements: "))
    print(f"Number of elements - {N_COUNT}, their sum - {cycle_method(N_COUNT)}")
except ValueError:
    print("You entered a wrong value. Try again.")


