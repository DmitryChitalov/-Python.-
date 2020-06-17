mass = [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]

idx_min_1 = 0
idx_min_2 = 0
answ = 0

for idx in range(len(mass)):
    if mass[idx_min_1] > mass[idx] and mass[idx_min_1] <= mass[idx_min_2]:
        idx_min_1 = idx
    elif mass[idx_min_2] > mass[idx]:
        idx_min_2 = idx

count_min_num = 0
for el in mass:
    if el == mass[idx_min_1]:
        count_min_num += 1
print(f'Наименьший элемент: {mass[idx_min_1]}, встречается в этом массиве {count_min_num} раз')
print(f'Второй наименьший элемент: {mass[idx_min_2]}')
