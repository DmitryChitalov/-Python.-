"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
Для извлечения цифр числа используйте арифм. операции

Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


while True:
    break_point = False
    while True:
        num_user = input("Enter your number or 0 for exit: ")
        if num_user == '0':
            break_point = True
            break
        elif num_user.isdigit():
            break
        else:
            print("Invalid number. Repeat entry.")
    if break_point:
        break
    num_len = len(num_user)
    num_user = int(num_user)
    count_odd = 0               # нечетные
    count_even = 0              # четные
    for i in range(0, num_len):
        num_dig = (num_user // pow(10, i)) % 10
        if num_dig % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    print(f"In the number {num_user} there are {num_len} digits "
          f"of which {count_even} are even and {count_odd} are odd")
