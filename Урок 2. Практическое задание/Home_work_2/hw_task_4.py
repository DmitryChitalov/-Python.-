len_rd = int(input())
answ = 0
start = 1
for _ in range(len_rd):
    answ += start
    start /= -2

print(f'Длинна последовательности: {len_rd}; их сумма равна: {answ}')
