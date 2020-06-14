def calculator():
    operation_sign = input('Enter operation sign or "0" for exit: ')
    if operation_sign == '0':
        print('Process completed.')
    elif not operation_sign == '+' \
            and not operation_sign != '-' \
            and not operation_sign != '*' \
            and not operation_sign != '/':
        print('Unknown operation sign. Try again, please.')
    else:
        num_a = input('Enter the first number: ')
        num_b = input('Enter the second number: ')
        if num_a.isdigit() and num_b.isdigit():
            if operation_sign == '+':
                result = int(num_a) + int(num_b)
                print(f'Result: {num_a} + {num_b} = {result}')
            elif operation_sign == '-':
                result = int(num_a) - int(num_b)
                print(f'Result: {num_a} - {num_b} = {result}')
            elif operation_sign == '*':
                result = int(num_a) * int(num_b)
                print(f'Result: {num_a} * {num_b} = {result}')
            elif operation_sign == '/':
                if not num_b == '0':
                    result = int(num_a) / int(num_b)
                    print(f'Result: {num_a} / {num_b} = {result}')
                else:
                    print('Division by 0 is not supported.')
        else:
            print('Invalid data, enter again.')
        return calculator()

calculator()
