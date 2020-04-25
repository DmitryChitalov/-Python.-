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
# ввод
NUMBER = int(input('Введите число\n'))

# определение
def recur(number, digit=""):
    """ тут какое-то описсание функции"""
    if number == 0:
        return digit
    else:
        digit = str(number % 10)
        return digit + str(recur(number // 10))

# поехали
print(recur(NUMBER))
