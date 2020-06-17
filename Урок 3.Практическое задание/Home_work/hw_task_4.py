mass = [88, 3, 26, 41, 75, 23, 3, 52, -49, 60, 69, -18, 3]
len_mass = len(mass)
number = mass[0]
max_count = 1
for el_idx in range(len_mass - 1):
    count = 1
    for idx in range(el_idx + 1, len_mass):
        if mass[el_idx] == mass[idx]:
            count += 1
    if count > max_count:
        max_count = count
        number = mass[el_idx]

print(f'{max_count} раз встречается число - {number}')
