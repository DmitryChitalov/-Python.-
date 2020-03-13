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

Решил не использовать функции chr() и ord(), т.к. в задачи стоит огнаничение по алфавиту,
т.е. требуется еще контролировать это условие.
"""

if __name__ == "__main__":

    print(f"{'='*10} Демонстрация решения 5-й задачи")

    # Алфавит
    ALPHA_ENG = 'abcdefghijklmnopqrstuvwxyz'

    LETTE_1 = input("Введите первую букву латинского алфавита:").lower()
    LETTE_2 = input("Введите вторую букву латинского алфавита:").lower()

    if len(LETTE_1) == len(
            LETTE_2) == 1 and LETTE_1 in ALPHA_ENG and LETTE_2 in ALPHA_ENG:
        PLACE1 = ALPHA_ENG.find(LETTE_1) + 1
        PLACE2 = ALPHA_ENG.find(LETTE_2) + 1
        print(f"Первая буква стоит на {PLACE1}-м месте в алфавите")
        print(f"Вторая буква стоит на {PLACE2}-м месте в алфавите")
        print(
            f"Между ним находяться {abs((PLACE2-PLACE1 if PLACE2!=PLACE1 else 1))-1} букв")
    else:
        raise ValueError(
            "Ошибка. Значения не являются буквами латинского алфафита")
