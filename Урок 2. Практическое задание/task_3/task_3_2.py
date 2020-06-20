def num_reverse(num_a, num_b):
    if num_a == 0:
        return f'Reversed num: {num_b}'
    else:
        tmp = num_a % 10
        return num_reverse(num_a // 10, str(num_b) + str(tmp))

print(num_reverse(int(input('Input number for reverse: ')), ' '))
