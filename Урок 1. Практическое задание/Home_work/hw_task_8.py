year = int(input())
if (year % 4 == 0 and year % 100 == 0) or year % 400 == 0:
    print('Год весокосный.')
else:
    print('Год не весокосный')

answ = 'Год весокосный.' if (year % 4 == 0 and year % 100 == 0) or year % 400 == 0 else 'Год не весокосный'
print('---------')
print(answ)
