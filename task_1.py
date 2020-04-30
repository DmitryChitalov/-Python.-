"""
Задание_1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

Подсказка: используйте вложенный цикл

Пример:
В диапазоне 2-99: 49 чисел кратны 2
В диапазоне 2-99: 33 чисел кратны 3
В диапазоне 2-99: 24 чисел кратны 4
В диапазоне 2-99: 19 чисел кратны 5
В диапазоне 2-99: 16 чисел кратны 6
В диапазоне 2-99: 14 чисел кратны 7
В диапазоне 2-99: 12 чисел кратны 8
В диапазоне 2-99: 11 чисел кратны 9
"""
def task_one():
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    for elem in range(2, 100):
        for el in range(2, 10):
            if elem % el == 0 and el == 2:
                two += 1
            if elem % el == 0 and el == 3:
                three += 1
            if elem % el == 0 and el == 4:
                four += 1
            if elem % el == 0 and el == 5:
                five += 1
            if elem % el == 0 and el == 6:
                six += 1
            if elem % el == 0 and el == 7:
                seven += 1
            if elem % el == 0 and el == 8:
                eight += 1
            if elem % el == 0 and el == 9:
                nine += 1
    print(f"two = {two}\nthree = {three}\nfour = {four}\nfive = {five}\n"
          f"six = {six}\nseven = {seven}\neight = {eight}\nnine = {nine}")


task_one()
