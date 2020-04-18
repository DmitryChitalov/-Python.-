"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

from collections import defaultdict
import sys
import random

# print (sys.version)
# Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
# Windows-10-10.0.18362-SP0 x64

# Основной принцип: внутри функции выводим все локальные переменные через locals() и просчитываем каждую через
# функцию show_size().


def show_size(x, level=0):
    result_size = sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                result_size += show_size(key, level + 1)
                result_size += show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                result_size += show_size(item, level + 1)
    return result_size


# Анализ из задания 6 для 1-го урока. Буква по номеру
# Вариант 1. Через массив.
def find_letter_list(number_letter):
    alphabet = [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z']
    local_variables_dict = locals().copy()  # Копируем
    # Так как последующие переменные были заданы после вызова функции copy, то можно сказать, что это будет размер,
    # занимаемый переменными в чистом виде.
    print(f'Список всех переменных: {local_variables_dict}')
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
        size_of_all_variables += show_size(local_variables_dict[var])
    print(
        f'Общий размер используемых переменных в функции {find_letter_list.__name__}: {size_of_all_variables} байт')
    if number_letter <= 0 or number_letter > len(alphabet):
        return 'error'
    else:
        return alphabet[number_letter - 1]


# Так как подсчёт идёт внутри функции, то надо её вызвать
print(f'Результат вызова функции: {find_letter_list(1)}')

# Общий размер используемых переменных в функции find_letter_list: 822 байт


# Вариант 2. Через цикл.
def find_letter_cycle(number_letter):
    string = 'abcdefghijklmnopqrstuvwxyz'
    result = 'error'
    for i, letter in enumerate(string):
        if i == (number_letter - 1):
            result = letter
            break
        elif i == len(string) - 1:
            result = 'error'
    local_variables_dict = locals().copy()
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
        size_of_all_variables += show_size(local_variables_dict[var])
    print(
        f'Общий размер используемых переменных в функции {find_letter_cycle.__name__}: {size_of_all_variables} байт')
    return result


print(f'Результат вызова функции: {find_letter_cycle(1)}')

# Общий размер используемых переменных в функции find_letter_cycle: 129 байт

# Анализ задания 2 из урока 5. Сложение и умножение шестнадцатиричных чисел
# Функция по сложению двух чисел.
def summary(number_sum, number_sum_2):
    result_list = []
    # Переворачиваем числа, чтобы легче было складывать
    rev_number_1 = number_sum[::-1]
    rev_number_2 = number_sum_2[::-1]
    if len(rev_number_1) > len(rev_number_2):  # Приравниваем длину чисел
        rev_number_2 = rev_number_2 + '0' * \
            (len(rev_number_1) - len(rev_number_2))
    else:
        rev_number_1 = rev_number_1 + '0' * \
            (len(rev_number_2) - len(rev_number_1))
    in_mind = 0
    for index, digit in enumerate(
            rev_number_1):  # Проходимся по циклу из числа 1 и складываем в столбик
        result = my_converter[digit] + \
            my_converter[rev_number_2[index]] + in_mind
        if result > 16:  # Запоминаем, если надо
            in_mind = result // 16
        else:
            in_mind = 0
        current_result = result - 16 * in_mind
        # Получаем результат для сложения
        result = my_converter_reverse[str(current_result)]
        result_list.append(result)
    # Переворачиваем массив обратно
    local_variables_dict = locals().copy()
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
        size_of_all_variables += show_size(local_variables_dict[var])
    print(
        f'Общий размер используемых переменных в функции {summary.__name__}: {size_of_all_variables} байт')
    return list(reversed(result_list))


# Функция по произведению двух чисел
def multiplication(number_multi, number_multi_2):
    rev_number_1 = number_multi[::-1]
    rev_number_2 = number_multi_2[::-1]
    list_of_results = []
    # Проходимся числу, которое умножает
    for index, digit_2 in enumerate(rev_number_2):
        result_middle_list = []
        in_mind = 0
        for digit in rev_number_1:
            # Получаем результат умножения
            result_middle = my_converter[digit] * \
                my_converter[digit_2] + in_mind
            if result_middle > 16:
                in_mind = result_middle // 16
            else:
                in_mind = 0
            current_result = result_middle - 16 * in_mind
            result = my_converter_reverse[str(current_result)]
            result_middle_list.append(result)
        if in_mind != 0:
            result_middle_list.append(str(in_mind))
        var_1 = list(reversed(result_middle_list))
        for j in range(
                index):  # Необходимо добавить нули для корректного последующего сложения столбиком
            var_1.append('0')
        # Получаем массив с числами, которые нужно сложить
        list_of_results.append(var_1)
    for var_2 in range(0, len(list_of_results) - 1, 1):
        number_first = ''.join(list_of_results[var_2])
        number_second = ''.join(list_of_results[var_2 + 1])
        # Складываем два числа в массиве
        calculation_result = summary(number_first, number_second)
        # Ставим результат во вторую позицию, чтобы следующее умножение было
        # как результат+следующее значение
        list_of_results[var_2 + 1] = calculation_result
    # Возвращаем последнее значение
    local_variables_dict = locals().copy()
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
        size_of_all_variables += show_size(local_variables_dict[var])
    print(
        f'Общий размер используемых переменных в функции {multiplication.__name__}: {size_of_all_variables} байт')
    return list_of_results[len(list_of_results) - 1]


# Из строчного значения в шестнадцатиричной получаем значение в десятичной.
my_converter = defaultdict(list,
                           {'0': 0,
                            '1': 1,
                            '2': 2,
                            '3': 3,
                            '4': 4,
                            '5': 5,
                            '6': 6,
                            '7': 7,
                            '8': 8,
                            '9': 9,
                            'A': 10,
                            'B': 11,
                            'C': 12,
                            'D': 13,
                            'E': 14,
                            'F': 15})
# Из строчного значения десятичной системы получаем строчное в шестнадцатиричной.
# Он ещё был нужен, потому что не нашёл простых методов получения значения
# из ключа для словаря.
my_converter_reverse = defaultdict(list,
                                   {'0': '0',
                                    '1': '1',
                                    '2': '2',
                                    '3': '3',
                                    '4': '4',
                                    '5': '5',
                                    '6': '6',
                                    '7': '7',
                                    '8': '8',
                                    '9': '9',
                                    '10': 'A',
                                    '11': 'B',
                                    '12': 'C',
                                    '13': 'D',
                                    '14': 'E',
                                    '15': 'F'})

number_1 = input('Введите первое число: ')
number_2 = input('Введите второе число: ')


# Для теста были взяты значения A2 и C4FF

print('Сумма чисел:', summary(number_1, number_2))
# Общий размер используемых переменных в функции summary: 431 байт

print('Произведение чисел:', multiplication(number_1, number_2))
# Общий размер используемых переменных в функции multiplication: 1629 байт

