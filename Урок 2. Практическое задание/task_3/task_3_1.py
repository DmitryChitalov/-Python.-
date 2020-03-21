"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
Используйте арифм операции для формирования числа, обратного введенному

Пример:
Введите число: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
import sys

CONVERTED_NUMBER = ""
try:
    USER_NUMBER = int(input("Введите число: "))
except ValueError:
    print("Неверный ввод числа")
    sys.exit()

while USER_NUMBER != 0:
    CONVERTED_NUMBER = CONVERTED_NUMBER + str(USER_NUMBER % 10)
    USER_NUMBER = USER_NUMBER // 10
print(CONVERTED_NUMBER)
