# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6. 
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

a = 5 # '101'
b = 6 # '110'

print (f'Binary AND is {a & b}') # '100'
print (f'Binary OR is {a | b}') # '111'
print (f'Binary XOR is {a ^ b}') # '011'

print (f'Binary shift 2 bits right is {a >> 2}') # '1'
print (f'Binary shift 2 bits left is {a << 2}') # '10100'

