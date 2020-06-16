def sum_of_el(cutter, current_num, tmp):
    if cutter == 0:
        return f'The sum of the specified number of elements is equal to: {tmp}'
    else:
        return sum_of_el(cutter - 1, current_num / -2, tmp + current_num)

print(sum_of_el((int(input('Enter the number of items: '))), 1, 0))
