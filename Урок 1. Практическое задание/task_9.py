"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
#VAR_1

print("Все числа должны быть разными!!!")
NUMB_A = int(input("Введите первое число: "))
NUMB_B = int(input("Введите второе число: "))
NUMB_C = int(input("Введите третье число: "))

LIST = [NUMB_A, NUMB_B, NUMB_C]
LIST = sorted(LIST)
print("ПЕРВЫЙ ВАРИАНТ")
print(f'Среднее число: {LIST[1]}')
#VAR_2
print("ВТОРОЙ ВАРИАНТ")
if NUMB_A != NUMB_B or NUMB_A != NUMB_C or NUMB_B != NUMB_C:
    if NUMB_A > NUMB_B > NUMB_C:
        print(f"{NUMB_B} - среднее число")
    elif NUMB_B > NUMB_C > NUMB_A:
        print(f"{NUMB_C} - среднее число")
    elif NUMB_C > NUMB_A > NUMB_B:
        print(f"{NUMB_A} - среднее число")
    elif NUMB_A < NUMB_B < NUMB_C:
        print(f"{NUMB_B} - среднее число")
    elif NUMB_B < NUMB_C < NUMB_A:
        print(f"{NUMB_C} - среднее число")
    elif NUMB_C < NUMB_A < NUMB_B:
        print(f"{NUMB_A} - среднее число")
else:
    print("Вы ввели равные числа")