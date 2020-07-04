import datetime
import random

user_data_1 = input('Enter the beginning '
                    'of the range for a random value: ')
user_data_2 = input('Enter end of range for random value: ')

now = datetime.datetime.now()
tmp = now.microsecond

try:
    if user_data_1.isalpha() and user_data_2.isalpha():
        if len(user_data_1) == 1 and len(user_data_2) == 1:
            print('Пользователь ввел буквы.')
        else:
            print('Please, enter no more '
                  'than 1 letter in each input field.')
    elif user_data_1.isdigit() \
            and user_data_2.isdigit():
    else:
        try:
            start_num = float.user_data_1
            fin_num = float.user_data_2
        except(TypeError,ValueError):
            print('It seems that a random value '
                  'cannot be generated in a given range. '
                  'Try other introductory ones.')
except (TypeError, ValueError):
    print('Incorrect data. Try again. '
          'Use equal data type for range.')



