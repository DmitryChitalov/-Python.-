user_num = int(input('Input number for reverse: '))
reversed_num = ''

while not user_num == 0:
    tmp_num = user_num % 10
    reversed_num += str(tmp_num)
    user_num = user_num // 10

print(f'Reversed num: {reversed_num}')
