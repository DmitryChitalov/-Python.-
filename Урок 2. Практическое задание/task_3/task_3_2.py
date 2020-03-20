"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def revers(enter_num, revers_num=0):
    """
    Функция принимает в качестве аргумента число, которое преобразует таким образом,
    что в новом числе цифы располагаются в обратном порядке.

    Функция вызывается рекурсивно до тех пор, пока в ведённом числе есть цифры больше 0
    :param enter_num:
    :param revers_num:
    :return:
    """
    # Условие остановки рекурсивных вызовов - введённое число стало == 0
    if enter_num == 0:
        print(f'Число, с обратным порядком цифр: {int(revers_num)}')
        return
    num = enter_num % 10 # получение единиц из введённого числа
    revers_num = (revers_num + num / 10) * 10 # присоединение единиц в обратном порядке
    enter_num //= 10 # убрать обработанный порядок у исходного числа
    revers(enter_num, revers_num) # Рекурсивный вызов функции

try:
    ENTER_NUM = int(input('Введите целое число: ')) # Ввод исходного числа
    revers(ENTER_NUM)  # Вызов функции
except ValueError:
    print('Необходимо вводить число.')
