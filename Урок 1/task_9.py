A = input("Ведите первое число: ")
B = input("Ведите первое число: ")
C = input("Ведите первое число: ")

if B < A < C or C < A < B:
    print('Среднее:', A)
elif A < B < C or C < B < A:
    print('Среднее:', B)
else:
    print('Среднее:', C)
input("Press any to exit...")