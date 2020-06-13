num = int(input())
proverk = 0
for el in range(1, num + 1):
    proverk += el

if float(proverk) == num*(num+1)/2:
    print('Утверждение верное...')
else:
    print('Утверждение не верное...')
