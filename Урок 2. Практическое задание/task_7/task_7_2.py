"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def num_enter():
    num_user = input("Enter your number: ")
    if num_user.isdigit():
        return int(num_user)
    else:
        print("Invalid number. Repeat entry.")
        return num_enter()


def expression_1st(num_user):
    if num_user == 1:
        return 1
    return num_user + expression_1st(num_user - 1)


NUM_USER = num_enter()

EXPRESSION_1ST = expression_1st(NUM_USER)
expression_2nd = int(NUM_USER * (NUM_USER + 1) / 2)

print(f"Expression 1+2+...+n where n={NUM_USER} equally {EXPRESSION_1ST}")
print(f"Expression n(n+1)/2 where n={NUM_USER} equally {expression_2nd}")

if expression_2nd == EXPRESSION_1ST:
    print("These two expressions are equal")
else:
    print("These two expressions are not equal")
