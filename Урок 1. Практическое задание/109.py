user_num_1 = input('Enter 1st number: ')
user_num_2 = input('Enter 2nd number: ')
user_num_3 = input('Enter 3rd number: ')

try:
    if user_num_1.isdigit() and user_num_2.isdigit() and user_num_3.isdigit():
        if user_num_1 > user_num_2 > user_num_3 \
        or user_num_3 > user_num_2 > user_num_1:
            print(f'Middle value is: {user_num_2}')
        elif user_num_2 > user_num_1 > user_num_3 \
        or user_num_3 > user_num_1 > user_num_2:
            print(f'Middle value is: {user_num_1}')
        elif user_num_2 > user_num_3 > user_num_1 \
        or user_num_1 > user_num_3 > user_num_2:
            print(f'Middle value is: {user_num_3}')
        else:
            print(f'There is no middle value among next values: '
                  f'{user_num_1}, {user_num_2} and {user_num_3}')
    else:
        print('Inputed data incorrect. Please, use numbers.')
except TypeError:
    print('Unsupported data type. Please, use numbers.')
