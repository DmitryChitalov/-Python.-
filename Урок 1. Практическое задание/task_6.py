"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.

Пример:
Введите номер буквы: 4
Введёному номеру соответствует буква: d

Подсказка: используйте ф-ции chr() и ord()
"""


try:
    user_char = chr(
                    int(
                        input("Please type the number of your char - ")
                    ) + ord("a") - 1
                )
    print(f"Your char is {user_char}.")
except ValueError:
    print("You entered an incorrect value.")
