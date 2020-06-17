"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
number = int(input('Введите число n: '))

left = 0

for i in range(1, number + 1):
    left += i

right = number * (number + 1) // 2

print(left)
print(right)

while True:
    if left == right:
        print('Равенство верно')
        break
    else:
        print('Равенство не верно')