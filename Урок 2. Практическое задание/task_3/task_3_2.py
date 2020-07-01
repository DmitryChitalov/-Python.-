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


# Solution from teacher

def recur_method(numb, flip=0):
    if numb == 0:
        return flip
    else:
        flip = (flip * 10) + (numb % 10)
        numb = numb // 10
        return recur_method(numb, flip)
try:
    NUMB = int(input("Enter a number: "))
    print(f"Inverted number is {recur_method(NUMB)}")
except ValueError:
    print("You entered a wrong value. Try again")