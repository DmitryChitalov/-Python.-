"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

while True:
    count = input("Enter the number of items: ")
    if count.isdigit():
        count = int(count)
        break
    else:
        print("Invalid number. Repeat entry.")

sum_el = 0

for i in range(0, count):
    if i % 2 == 0:
        sum_el += 1 / pow(2, i)
    else:
        sum_el -= 1 / pow(2, i)

print(f"Number of elements - {count}, their sum - {sum_el}")
