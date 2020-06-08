"""
Задание 5.
Пользователь вводит две буквы. Определить,
на каких местах алфавита они стоят, и сколько между ними находится букв.

Подсказка:
Вводим маленькие латинские буквы.
Обратите внимание, что ввести можно по алфавиту, например, a,z
а можно наоборот - z,a
В обоих случаях программа должна вывести корректный результат.
В обоих случаях он 24, но никак не -24
"""


class AlphabetCounter:
    def __init__(self):
        self.alphabet_symbols = 'abcdefghijklmnopqrstuvwxyz'

    def get_letter_position(self, letter: str):
        try:
            if letter == "":
                raise ValueError
            letter_position = self.alphabet_symbols.index(letter) + 1
        except ValueError:
            letter_position = -1
        return letter_position

    def get_num_letters_between(self, letter_1, letter_2):
        letter_1_position = self.get_letter_position(letter_1)
        letter_2_position = self.get_letter_position(letter_2)
        if letter_1_position == -1 or letter_2_position == -1:
            return -1
        if letter_1_position == letter_2_position:
            letters_between = 0
        else:
            letters_between = abs(letter_1_position - letter_2_position) - 1
        return letters_between


def main():
    try:
        letter_1 = input("Enter first letter: ").lower()
        letter_2 = input("Enter second letter: ").lower()
        counter = AlphabetCounter()
        letters_between = counter.get_num_letters_between(letter_1, letter_2)
        if letters_between == -1:
            raise SyntaxError
        print(letters_between)
    except SyntaxError:
        print("You must enter only letters from english alphabet")
    except ValueError as ve:
        print(ve)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
