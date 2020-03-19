"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def num_enter():
    num_user = input("Enter your number or 0 for exit: ")
    if num_user == '0':
        return
    elif num_user.isdigit():
        return int(num_user)
    else:
        print("Invalid number. Repeat entry.")
        num_enter()


def digit_count(num_user, num_len, count=0):
    if count == num_len:
        return
    num_dig = (num_user // pow(10, count)) % 10
    if num_dig % 2 == 0:
        global COUNT_EVEN
        COUNT_EVEN += 1
        digit_count(num_user, num_len, count + 1)
    else:
        global COUNT_ODD
        COUNT_ODD += 1
        digit_count(num_user, num_len, count + 1)


NUM_USER = num_enter()
NUM_LEN = len(str(NUM_USER))
COUNT_ODD = 0               # нечетные
COUNT_EVEN = 0              # четные

digit_count(NUM_USER, NUM_LEN)
print(f"In the number {NUM_USER} there are {NUM_LEN} digits "
      f"of which {COUNT_EVEN} are even and {COUNT_ODD} are odd")
