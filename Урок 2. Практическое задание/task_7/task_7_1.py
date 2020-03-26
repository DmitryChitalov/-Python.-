"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

while True:
    num_user = input("Enter number: ")
    if num_user.isdigit():
        num_user = int(num_user)
        break
    else:
        print("Invalid number. Repeat entry.")

expression_1st = 0
for i in range(1, num_user + 1):
    expression_1st += i

expression_2nd = int(num_user * (num_user + 1) / 2)

print(f"Expression 1+2+...+n where n={num_user} equally {expression_1st}")
print(f"Expression n(n+1)/2 where n={num_user} equally {expression_2nd}")

if expression_2nd == expression_1st:
    print("These two expressions are equal")
else:
    print("These two expressions are not equal")
