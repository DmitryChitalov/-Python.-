matr = []

for count in range(5):
    matr.append([])
    sum_num = 0
    print(f'Введите элементы {count + 1}- строки: ')
    for _ in range(4):
        el = int(input())
        sum_num += el
        matr[count].append(el)
    matr[count].append(sum_num)

print('-----------')
for el in matr:
    print(*el)
