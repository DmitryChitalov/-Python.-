# Задание 2.
# Реализуйте два алгоритма.
# Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
# В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
# Сложность такого алгоритма: O(n^2) - квадратичная.
# Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
# Сложность такого алгоритма: O(n) - линейная.

# 1
import random as rnd
int_list = [rnd.randint(0, 1000) for p in range(0, 20)]
print(int_list)
result = int_list[0]
for el in int_list:
    if result >  el:
        result = el
print(result)

# 2
import random as rnd
int_list = [rnd.randint(0, 1000) for p in range(0, 20)]
print(int_list)
print(sorted(int_list)[0])
