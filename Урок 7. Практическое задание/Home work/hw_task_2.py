from random import random


def merger(mass):
    if len(mass) < 2:
        return mass[:]
    else:
        left_mass = merger(mass[:len(mass) // 2])
        right_mass = merger(mass[len(mass) // 2:])
        return merger_help(left_mass, right_mass)


def merger_help(left_side, right_side):
    answ = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left_side) and right_idx < len(right_side):
        if left_side[left_idx] < right_side[right_idx]:
            answ.append(left_side[left_idx])
            left_idx += 1
        elif left_side[left_idx] > right_side[right_idx]:
            answ.append(right_side[right_idx])
            right_idx += 1
        else:
            answ.append(right_side[right_idx])
            answ.append(left_side[left_idx])
            right_idx += 1
            left_idx += 1
    while left_idx < len(left_side):
        answ.append(left_side[left_idx])
        left_idx += 1
    while right_idx < len(right_side):
        answ.append(right_side[right_idx])
        right_idx += 1
    return answ


def rand(len_mass):
    right = 0
    left = 50
    mass = [float(random() * (right - left)) + left for _ in range(len_mass)]
    return mass


len_my_mass = int(input('Введите длинну массива: '))
massive = rand(len_my_mass)
print(massive)
massive = merger(massive)
print(massive)
