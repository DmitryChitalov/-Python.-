num = int(input())
a = num // 100
b = (num // 10) % 10
c = num % 10

print(f'Сумма цифр: {a+b+c}')
print(f'Произведение цифр: {a*b*c}')

