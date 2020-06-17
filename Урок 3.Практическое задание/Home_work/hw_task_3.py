mass = [88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
print(mass)
idx_min = 0
idx_max = 0
for idx in range(len(mass)):
    if mass[idx_max] < mass[idx]:
        idx_max = idx
    elif mass[idx_min] > mass[idx]:
        idx_min = idx

mass[idx_min], mass[idx_max] = mass[idx_max], mass[idx_min]
print(mass)
