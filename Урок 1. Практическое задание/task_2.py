"""
Задание 2. Выполнить логические побитовые операции "И", "ИЛИ"
и др. над числами 5 и 6. Выполнить
над числом 5 побитовый сдвиг вправо и влево на два знака.

Подсказка: это стандартные операции, которые осуществляются с помощью
стандартных операторов. Попробуйте найти каких именно.
"""

n1 = 5
n2 = 6

bit_or = n1 | n2
bit_and = n1 & n2
bit_xor = n1 ^ n2

print(f"Bit or of 5 and 6 = {bit_or}")
print(f"Bit and of 5 and 6 = {bit_and}")
print(f"Bit xor of 5 and 6 = {bit_xor}")

print(f"{n1} bit shift to left by 2 places {n1 << 2}")
print(f"{n1} bit shift to left by 2 places {n1 >> 2}")

print(f"{n2} bit shift to left by 2 places {n2 << 2}")
print(f"{n2} bit shift to left by 2 places {n2 >> 2}")
