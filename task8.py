# Определить, является ли год, который ввел пользователем, високосным или не високосным.

year = int(input('Please provide Year number as 4 digits value: ').rstrip().lstrip())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} is leap year')
else:
    print(f'{year} is not leap year')
