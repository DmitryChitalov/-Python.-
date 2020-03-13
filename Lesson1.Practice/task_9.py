"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

print("Введите 3 числа для сравнения")
NUM1 = int(input("Первое число: "))
NUM2 = int(input("Второе число: "))
NUM3 = int(input("Третье число: "))
if NUM1 == NUM2 and NUM1 == NUM3:
    print("Вы ввели 3 равные числа")
elif NUM2 < NUM1 < NUM3 or NUM2 > NUM1 > NUM3:
    print(NUM1)
elif NUM1 > NUM2 > NUM3 or NUM1 < NUM2 < NUM3:
    print(NUM2)
else:
    print(NUM3)