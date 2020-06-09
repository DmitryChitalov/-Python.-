alph = 'abcdefghijklmnopqrstuvwxyz'

first_b = input().lower()
second_b = input().lower()

print(abs(alph.find(second_b) - alph.find(first_b)) - 1)
