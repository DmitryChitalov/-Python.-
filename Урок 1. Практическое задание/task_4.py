"""
Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

Подсказка:
Нужно обойтись без ф-ций randint() и uniform()
Использование этих ф-ций = задание не засчитывается

Функцию random() использовать можно
Опирайтесь на пример к уроку
"""
import random

DIAP1_1 = int(input("Введите минимальное значение целого числа: "))
DIAP1_2 = int(input("Введите максимальное значение целого числа: "))

if len(str(DIAP1_2)) > len(str(DIAP1_1)):
    GEN = random.random() * (DIAP1_2 - DIAP1_1 + 1) + DIAP1_1
else:
    GEN = random.random() * (DIAP1_1 - DIAP1_2 + 1) + DIAP1_2


print(round(GEN))

DIAP2_1 = int(input("Введите минимальное значение вещественного числа: "))
DIAP2_2 = int(input("Введите максимальное значение вещественного числа: "))

if len(str(DIAP2_2)) > len(str(DIAP2_1)):
    ZERO = len(str(DIAP2_2))
else:
    ZERO = len(str(DIAP2_1))

mult = int('1'+ ZERO*'0')

while True:
    if DIAP2_1 <=0:
        GEN = random.random() * mult * -1
        if DIAP2_1 <= GEN <= DIAP2_2:
            break
        GEN = random.random() * mult
        if DIAP2_1 <= GEN <= DIAP2_2:
            break

    else:
        GEN = random.random() * mult
        if DIAP2_1 <= GEN <= DIAP2_2:
            break

print(GEN)

DIAP3_1 = input("Введите первый символ: ")
DIAP3_2 = input("Введите второй символ: ")

DIAP3_1 = ord(DIAP3_1)
DIAP3_2 = ord(DIAP3_2)

GEN = round(random.random() * (DIAP3_2 - DIAP3_1 + 1) + DIAP3_1)
print(chr(GEN))