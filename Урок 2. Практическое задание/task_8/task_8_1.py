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
"""
how_many_number = int(input('Сколько будет чисел?  '))
while True:
    figure = input('Какую цифру считать ')
    if int(figure) > 0 and int(figure) < 10:
        break
    else:
        print('Ошибка. Нужна цифра от 1 до 9')

count = 0

for idx in range(how_many_number):
    number = list(input(f'Число {idx+1}: '))

    for user_figure in number:

        if user_figure == figure:
            count+=1

print(f'Было введено {count} цифр "{figure}"')

