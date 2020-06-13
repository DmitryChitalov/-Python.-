num = int(input('Number: '))
chet = 0
ne_chet = 0
for el in str(num):
    if int(el) % 2 == 0:
        chet += 1
    else:
        ne_chet += 1
print(f'Чётных чисел: {chet}; нечётных: {ne_chet}')
