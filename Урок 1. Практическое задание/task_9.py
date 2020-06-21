"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

env1 = int(input("Введите 1ое число :\t"))
env2 = int(input("Введите 2ое число :\t"))
env3 = int(input("Введите 3ее число :\t"))

if env1 < env2 < env3 or env3 < env2 < env1:
    medium = env2
elif env2 < env1 < env3 or env3 < env1 < env2:
    medium = env1
else:
    medium = env3
print(medium)