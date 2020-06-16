user_letter_num = input('Enter number of a letter: ')

try:
    if 65 <= user_letter_num + 64 <= 90:
        print(chr(user_letter_num + 64))
    else:
        print('There is no letter in alphabet with such number.')
except TypeError:
    print(f'{user_letter_num} - is unsupported data type. '
          f'Try number in range "1 - 26".')
