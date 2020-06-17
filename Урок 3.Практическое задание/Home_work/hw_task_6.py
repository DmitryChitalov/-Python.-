mass = [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
idx_min = 0
idx_max = 0
answ = 0

for idx in range(len(mass)):
    if mass[idx_max] < mass[idx]:
        idx_max = idx
    elif mass[idx_min] > mass[idx]:
        idx_min = idx


if idx_min < idx_max:
    for idx in range(idx_min + 1, idx_max):
        answ += mass[idx]
else:
    for idx in range(idx_max + 1, idx_min):
        answ += mass[idx]
print(f'Сумма элементов между минимальным ({mass[idx_min]})  и максимальным ({mass[idx_max]}) элементами: {answ}')

