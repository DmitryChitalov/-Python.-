"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

# Solution 1
import random

random_digit = random.randint(0, 100)
counter = 10

while counter > 0:
    users_number = int(input('Please try to guess a number: '))
    if users_number != random_digit:
        print('Wrong number')
        if users_number > random_digit:
            print('The digit is less than entered. Try again')
        else:
            print('The digit is bigger than entered. Try again')
    elif users_number == random_digit:
        print('You won!')
        break
    counter -= 1
print(f'The right number was {random_digit}')



# Solution 2
# import random
# num = random.randint(0, 100)
# print('Guess a number during 10 attempts')
# for i in range(1,11):
#     answer = int(input(f'Attempt {i}: '))
#     if num < answer:
#         print('The number is less')
#     elif num > answer:
#         print('The number is bigger')
#     else:
#         print(f'You guessed from {i} attempt! You won!')
#         break
# else:
#     print(f'You failed. it was {num}')


