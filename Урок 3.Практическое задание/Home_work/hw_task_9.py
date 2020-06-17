row = int(input('Введите кол. строк: '))
col = int(input('Введите кол. столбиков: '))
# matr = [[36, 20, 42, 38],
#         [46, 27,  7, 33],
#         [13, 12, 47, 15]]
matr = []
for count in range(row):
    matr.append([])
    print(f'Введите элементы {count + 1}- строки: ')
    for _ in range(col):
        el = int(input())
        matr[count].append(el)

numb = []
for idx_col in range(col):
    min_num = matr[0][idx_col]
    for idx_row in range(row):
        if min_num > matr[idx_row][idx_col]:
            min_num = matr[idx_row][idx_col]
    numb.append(min_num)

print(max(numb))
