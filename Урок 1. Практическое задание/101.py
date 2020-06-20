user_num = int(input('Введите число: '))

num_a = user_num // 100
num_b = ((user_num // 10) % 10)
num_c = user_num % 10

abc_sum = num_a + num_b + num_c
abc_product = num_a * num_b * num_c

print(f'Sum of entered numbers: {abc_sum}')
print(f'Product of numbers entered: {abc_product}')
