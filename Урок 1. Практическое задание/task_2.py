"""
Задание 2. Выполнить логические побитовые операции "И", "ИЛИ"
и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

Подсказка: это стандартные операции, которые осуществляются с помощью
стандартных операторов. Попробуйте найти каких именно.
"""

num_1 = 5
print(bin(num_1))
num_2 = 6
print(bin(num_2))

# Bit operation INVERSE
print('Print result for Inverse operation')
num_1_inv = ~num_1
num_2_inv = ~num_2
print(bin(num_1_inv))
print(bin(num_2_inv))

# Bit operation AND
print('Print result for AND operation')
print(num_1 & num_2)
print(bin(num_1 & num_2))

# Bit operation XOR
print('Print result for XOR operation')
print(num_1 ^ num_2)
print(bin(num_1 ^ num_2))

# Bit operation OR
print('Print result for OR operation')
print(num_1 | num_2)
print(bin(num_1 | num_2))

# Bit operation left shift
print('Print result for left shift operation')
print(bin(num_1 << 2))
print(bin(num_2 << 2))

# Bit operation right shift
print('Print result for right shift operation')
print(bin(num_1 >> 2))
print(bin(num_2 >> 2))


# над числом 5 побитовый сдвиг вправо и влево на два знака
print(num_1 << num_2)
print((num_1 * 2**num_2))

print(num_1 >> num_2)
print((num_1) // 2 ** num_2)
