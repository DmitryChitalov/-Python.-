user_letter_1 = input('Enter 1st letter: ')
user_letter_2 = input('Enter 2nd letter: ')


try:
    letter_a = ord(user_letter_1.lower())
    letter_b = ord(user_letter_2.lower())
    if  letter_a > letter_b:
        print(f'The letter {user_letter_1} has position {letter_a - 96},'
              f'the letter {user_letter_2} has position {letter_b - 96}'
              f' in alphabet. Letter spacing is {(letter_a - letter_b) - 1}.')
    else:
        print(f'The letter {user_letter_1} '
              f'has position {letter_a - 96}, '
              f'the letter {user_letter_2} '
              f'has position {letter_b - 96} in alphabet. '
              f'Letter spacing is {(letter_b - letter_a) - 1}.')
except TypeError:
    print('The entered data is incorrect. Try again.')
