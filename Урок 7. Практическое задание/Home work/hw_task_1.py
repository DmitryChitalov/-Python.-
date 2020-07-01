from random import randint
import time


def revers_bubble(mass):
    for i in range(len(mass) - 1):
        plase = True
        for j in range(len(mass) - 1, i, -1):
            if mass[j] < mass[j - 1]:
                mass[j], mass[j - 1] = mass[j - 1], mass[j]
                plase = False
        if plase:
            break
    return mass


def revers_bubble_new(mass):
    for i in range(len(mass) - 1):
        plase = True
        for j in range(len(mass) - 1, i, -1):
            if mass[j] < mass[j - 1]:
                mass[j], mass[j - 1] = mass[j - 1], mass[j]
                plase = False
        if plase:
            break
    return mass


len_my_mass = int(input('Введите длинну массива: '))
massive_1 = [randint(1, 20) for _ in range(len_my_mass)]
massive_2 = list(massive_1)
print(massive_1)
start = time.time()
massive_1 = revers_bubble(massive_1)
print(f'Работа пузырька без улучшения: {time.time() - start}')

start = time.time()
massive_2 = revers_bubble(massive_2)
print(f'Работа пузырька c улучшением: {time.time() - start}')
