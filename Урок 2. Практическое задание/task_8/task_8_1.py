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

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
number_len = int(input('Enter the length of the number: '))
counted_num = int(input('Enter the number you are looking for: '))
counter = 0
user_num = int(input('Enter number: '))
num_copy = user_num


while number_len != 0:
    current_num = user_num % 10
    if current_num == counted_num:
        counter += 1
    user_num = user_num // 10
    number_len -= 1


print(f'Among {num_copy}, the number {counted_num} occurs {counter} times.')
