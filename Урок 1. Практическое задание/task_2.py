"""
Задание 2. Выполнить логические побитовые операции "И", "ИЛИ"
и др. над числами 5 и 6. Выполнить
над числом 5 побитовый сдвиг вправо и влево на два знака.

Подсказка: это стандартные операции, которые осуществляются с помощью
стандартных операторов. Попробуйте найти каких именно.
"""

bit_and = 5 & 6
bit_or = 5 | 6
bit_xor = 5 ^ 6
print(bit_and, bit_or, bit_xor)

a = 5 << 2
b = 5 >> 2
print(a, b)