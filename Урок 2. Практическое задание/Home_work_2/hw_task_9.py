count_num = int(input('Введите количество чисел: '))
max_sum = 0
max_num = 0
for _ in range(count_num):
    sum_in_num = 0
    num = input('Введите число: ')
    for el in num:
        sum_in_num += int(el)
    if sum_in_num > max_sum:
        max_num = int(num)
        max_sum = sum_in_num
print(f'{max_num} с самой большой суммой цифр ({max_sum})')
