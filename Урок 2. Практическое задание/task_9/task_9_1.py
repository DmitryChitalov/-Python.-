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

def recurs(num):
    global summ, text, local_summ
# Не пойму почему, но полностью ошибочная логиска рекурсии
    if num < 10:
        local_summ = local_summ + num
        if local_summ > summ:
            summ = local_summ
            text = f'Наибольшее число по сумме цифр: {num}, сумма его цифр: {summ}'
            return text, summ
        else:
            return
    else:
        local_summ = local_summ + num % 10
        return recurs(num // 10)


while True:
    print('Для завершения программы введите 0')
    summ, local_summ = 0, 0
    text = ''

    try:
        n = int(input('Введите количество чисел: '))
    except Exception as e:
        print('Вы должны ввести натуральное число!')
        continue

    if n == 0:
        print('Программа завершена!')
        break

    while n != 0:
        try:
            num = int(input('Введите очередное число: '))
        except Exception as e:
            print('Вы должны ввести натуральное число!')
            break
        n -= 1

        if num < 10 and num > summ:
            summ = num
            text = f'Наибольшее число по сумме цифр: {num}, сумма его цифр: {num}'
        else:
            recurs(num)

    print(text)
