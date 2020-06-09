from random import random
alph = 'abcdefghijklmnopqrstuvwxyz'

# №1
left = int(input())
right = int(input())

answ = int(random() * (right - left + 1)) + left
print(answ)

# №2
right = float(input())
left = float(input())

answ = float(random() * (right - left)) + left
print(answ)

# №3
left_b = input().lower()
right_b = input().lower()
left_b = alph.find(left_b)
right_b = alph. find(right_b)

answ = alph[int(random() * (right_b - left_b + 1)) + left_b]
print(answ)
