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

#Solution 1
# number = input('Enter you number: ')
# list_digits = list(map(int, str(number)))
# new = int
# new_list = []
#
# while len(list_digits) > 0:
#     new = list_digits[-1]
#     new_list.append(new)
#     list_digits.remove(new)
# print(int(''.join(map(str, new_list))))


#Solution 2
# BASE = 10
# num = input('Enter you number: ')
# result = 0
# while num > 0:
#     result = result * BASE + num % BASE
#     num = num // BASE
# print(result)


#Solution 3 - will consume RAM
# num = input('Enter you number: ')
# result = ''
# for i in num:
#     result = i + result
# print(result)


#Solution 4 - without cylce
# num = input('Enter you number: ')
# result = num[::-1]
# print(result)


#Solution from teacher


def cycle_method(numb):
    flip = 0
    while numb != 0:
        flip = (flip * 10) + (numb %10)
        numb = numb //10
    return flip

try:
    NUMB = int(input("Enter a number: "))
    print(f"Inverted number is {cycle_method(NUMB)}")
except ValueError:
    print("You entered a wrong value. Try again")






