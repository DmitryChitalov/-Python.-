"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
Пример:
строка: рара
подстроки:
рар
ра
р
а
ар
ара
Итог: 6 подстрок
"""


# Функция извлечения подстрок из строки
def find_substrings(string, substring='', start_index=0):
    """
    :param string: строка введеная пользователем
    :param substring: подстрока
    :param start_index: стартовый индекс в строке для поиска подстроки
    :return: список подстрок, количество подстрок
    """
    list_substrings = []
    length_string = len(string)
    while start_index != length_string:
        for alpha in string[start_index:]:
            substring = ''.join((substring, alpha))
            if substring not in list_substrings and substring != string:
                list_substrings.append(substring)
        start_index += 1
        substring = ''
    return list_substrings, len(list_substrings)


""" --------------------------------------------------- """


# Функция извлечения подстрок из строки с несколькими словами
def find_substrings_in_string(string, substring='', start_index=0):
    """
    :param string: строка введеная пользователем
    :param substring: подстрока
    :param start_index: стартовый индекс в строке для поиска подстроки
    :return: список подстрок, количество подстрок
    """
    list_substrings = []
    for word in string.split():
        while start_index != len(word):
            for alpha in word[start_index:]:
                substring = ''.join((substring, alpha))
                if substring not in list_substrings and substring != word:
                    list_substrings.append(substring)
            start_index += 1
            substring = ''
    return list_substrings, len(list_substrings)


""" --------------------------------------------------- """
STRING = input('Введите строку:\n').lower()

print(f'Список подстрок:')
for element in find_substrings(STRING)[0]:
    print(f'{element}')
print(f'Итого подстрок: {find_substrings(STRING)[1]}')
