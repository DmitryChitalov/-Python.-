"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
"""
NUMBER= int(input('Введите количество элементов:'))
TOTAL_SUM = 0

for el in range(NUMBER):
    TOTAL_SUM += el

if TOTAL_SUM==(NUMBER*(NUMBER-1)/2):
    print(f'Для множества натуральных чисел от 1 до {NUMBER} '
          f'выполняется равенство: 1+2+...+n = n(n+1)/2 ')
