try:
    user_data = int(input('Please enter the year in YYYY format: '))
    if user_data % 4 == 0:
        if user_data % 100 == 0:
            if user_data % 400 == 0:
                print('Leap year.')
            else:
                print('Not leap year.')
        else:
            print('Leap year.')
    else:
        print('Not leap year.')
except TypeError:
    print('Unsupported data type. Please, input year. For example: "1984".')
except ValueError:
    print('Incorrect value. Please, input year. For example: "1984".')