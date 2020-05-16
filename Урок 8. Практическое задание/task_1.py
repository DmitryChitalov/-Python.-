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


from hashlib import sha1


def get_dict_substring(string):
    """
    Функция ищет различные подстроки в строке и возвращает словарь хешей подстрок
    :param string: строка для поиска подстрок
    :return dict_substring: словарь хешей подстрок
    """
    len_string = len(string)  # вычисляем длину строки только один раз (для оптимизации)
    dict_substr = {}
    # ищем все возможные варианты подстрок
    for i in range(0, len_string + 1):
        for j in range(i + 1, len_string + 1):
            substr = string[i:j]
            # if substr == string: - для оптимизации перепишем условие
            if (not i) and j == len_string:  # не включаем строку целиком
                continue
            dict_substr[sha1(substr.encode('utf-8')).hexdigest()] = substr
    return dict_substr


def main():
    """
    основной код
    """
    string = input("Введите строку для поиска подстрок: ")
    dict_substring = get_dict_substring(string)
    print("Словарь хешей подстрок:")
    for k, val in dict_substring.items():
        print(f"{k} : {val}")
    print(f"Итог: {len(dict_substring)} подстрок")


# Понравилась идея из примера haffman_4.py всегда выделять код в отдельную функцию
# во-первых, прочитал о том, что такой код выполняется быстрее
# из-за особенностей хранения глобальных и локальных переменных в оперативной памяти
# во-вторых, pylint не ругается на наименования переменных в нижнем регистре
main()

# Результат выполнения программы:
# Введите строку для поиска подстрок: papa
# Словарь хешей подстрок:
# 516b9783fca517eecbd1d064da2d165310b19759 : p
# 379fc0d5299a71ac0f171fbb5afb262829b4e765 : pa
# 627a19572de5279b23ee9767fc5cf4b270625ac6 : pap
# 86f7e437faa5a7fce15d1ddcb9eaeaea377667b8 : a
# ac78b022715c5b8357b4dca8045e8463b4de2124 : ap
# 313212a1870215e863a9da1859fbaa6e53f50670 : apa
# Итог: 6 подстрок
