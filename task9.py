# Вводятся три разных числа. 
# Найти, какое из них является средним (больше одного, но меньше другого).

print('Plese provide 3 different numbers:')
n1 = float(input('\tn1 = '))
n2 = float(input('\tn2 = '))
n3 = float(input('\tn3 = '))

if (n1 > n2 and n1 < n3) or (n1 < n2 and n1 > n3):
    print(f'{n1} is between {n2} and {n3}')
elif (n2 > n3 and n2 < n1) or (n2 < n3 and n2 > n1):
    print(f'{n2} is between {n1} and {n3}')
elif (n3 > n1 and n3 < n2) or (n3 < n1 and n3 > n2):
    print(f'{n3} is between {n1} and {n2}')
else:
    print(f'All 3 numbers must be different')
