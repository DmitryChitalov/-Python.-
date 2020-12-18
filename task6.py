# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# способ 1
number = int(input('Please provide lowercase English alphabet letter number : ').lstrip().rstrip())
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
if number > 26 or number <= 0:
    print(f'Provided number is not valid, please retype: ')
else: 
    print(f'Your letter is {ascii_lowercase[number - 1]}')


# способ 2
number = int(input('Please provide lowercase English alphabet letter number : ').lstrip().rstrip())
mincode = 97
if number > 26 or number <= 0:
    print(f'Provided number is not valid, please retype: ')
else: 
    print(f'Your letter is {chr(mincode + number - 1)}')
