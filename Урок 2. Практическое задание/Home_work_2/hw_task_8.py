count_num = int(input('Количество чисел: '))
find_num = input('Какое ищем: ')
count_answ = 0
for _ in range(count_num):
    num = input('Введите число: ')
    for el in num:
        if find_num == el:
            count_answ += 1
print(f'Количество найденых чисел: {count_answ}')
        