"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
def num_counter(number, counted_num, number_len, counter):
    num_copy = user_num
    if number_len > 0:
        current_num = number % 10
        if current_num == counted_num:
            counter += 1
            number_len -= 1
        else:
            number_len -= 1
        num_counter(number // 10, counted_num, number_len - 1, counter)
    else:
        print(f'Among {num_copy}, the number {counted_num} occurs {counter} times.')


number_len = int(input('Enter the length of the number: '))
counted_num = int(input('Enter the number you are looking for: '))
user_num = int(input('Enter number: '))
num_counter(user_num, counted_num, number_len + 1, 0)
