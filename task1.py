# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

inp_str = input('Please provide 3 digit integer value : ').lstrip().rstrip()
if len(inp_str) != 3:
    print (f'It is not 3 digit integer value')
else:
    d1 = int(inp_str[0])
    d2 = int(inp_str[1])
    d3 = int(inp_str[2])
    print(f'Summa is : {d1 + d2 + d3}')
    print(f'Product is : {d1 * d2 * d3}')
