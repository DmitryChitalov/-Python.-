"""
Задание 2. Выполнить логические побитовые операции "И", "ИЛИ"
и др. над числами 5 и 6. Выполнить
над числом 5 побитовый сдвиг вправо и влево на два знака.

Подсказка: это стандартные операции, которые осуществляются с помощью
стандартных операторов. Попробуйте найти каких именно.
"""

BITNUM_1 = int('110', 2)
BITNUM_2 = int('101', 2)
print(f'BITNAM_1 = {BITNUM_1}')
print(f'BITNAM_2 = {BITNUM_2}')

BIT_OR = BITNUM_1 | BITNUM_2   # Побитовое ИЛИ
BIT_AND = BITNUM_1 & BITNUM_2   # Побитовое И
BIT_XOR = BITNUM_1 ^ BITNUM_2   # Побитовое ИСКЛЮЧАЮЩЕЕ ИЛИ
BIT_NOT = ~ BITNUM_2            # Побитовое НЕТ
SHIFT_L = BITNUM_1 << 2
SHIFT_R = BITNUM_1 >> 2

BIT_OR = bin(BIT_OR)
BIT_AND = bin(BIT_AND)
BIT_XOR = bin(BIT_XOR)
BIT_NOT = bin(BIT_NOT)
SHIFT_L = bin(SHIFT_L)
SHIFT_R = bin(SHIFT_R)


print(BIT_OR)
print(BIT_AND)
print(BIT_XOR)
print(BIT_NOT)
print(SHIFT_L)
print(SHIFT_R)
