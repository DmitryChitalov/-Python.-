user_num = int(input('Enter the number: '))
tmp_num = user_num
even = 0
not_even = 0
while not tmp_num == 0:
    tmp = tmp_num % 10
    if tmp % 2 == 0:
        even += 1
    else:
        not_even += 1
    tmp_num = tmp_num // 10


print(f'A number {user_num} is made up of {even + not_even} '
      f'numbers and has {even} even and {not_even} odd numbers.')
