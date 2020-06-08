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


class RandomLetter:
    def __init__(self):
        self.alphabet_symbols = 'abcdefghijklmnopqrstuvwxyz'

    def get_random_letter(self, start_symbol: str, stop_symbol: str):
        try:
            start_index = self.alphabet_symbols.index(start_symbol.lower())
            stop_index = self.alphabet_symbols.index(stop_symbol.lower()) + 1

            # if any([start_symbol, stop_symbol]) is None:      # Так красивее, но массивы нельзя =(
            if start_symbol is None or stop_symbol is None:
                raise NameError("Start/Stop letter is not a english alphabet letter!")
            if start_index > stop_index:
                raise IndexError("You should write start and stop symbols in alphabetical order!")

            random_index = int(random.random() * (stop_index - start_index)) + start_index
            random_letter = self.alphabet_symbols[random_index]
            return random_letter
        except NameError as ne:
            return ne
        except IndexError as ie:
            return ie
        except Exception as ex:
            return ex


def random_number(start, stop, int_num=True, float_nums=False):
    try:
        random_num = random.random() * (stop - start) + start
        if float_nums:
            return random_num
        elif int_num:
            return int(random_num)
        else:
            return None
    except Exception as ex:
        return ex


if __name__ == '__main__':
    # Test fo alphabet
    random_letter_instance = RandomLetter()
    random_letter = random_letter_instance.get_random_letter('B', 'O')
    print(random_letter)

    # test for random number
    # If you want to get float number do this -> float_num=True
    random_num_ = random_number(start=3, stop=76, float_nums=True)
    print(random_num_)

