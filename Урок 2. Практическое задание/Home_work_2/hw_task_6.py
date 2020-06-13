from random import random

left = 0
right = 100

answ = int(random() * (right - left + 1)) + left

for popitk in range(11):
    if popitk == 10:
        print(f'Вы проиграли, число: {answ}')
        exit()
    answ_polz = int(input())
    if answ == answ_polz:
        print('Вы победили!')
        exit()
    elif answ > answ_polz:
        print('Загаданное число больше...')
    elif answ < answ_polz:
        print('Загаданное число меньше...')