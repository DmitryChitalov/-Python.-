"""
Задание 2. Выполнить логические побитовые операции "И", "ИЛИ"
и др. над числами 5 и 6. Выполнить
над числом 5 побитовый сдвиг вправо и влево на два знака.

Подсказка: это стандартные операции, которые осуществляются с помощью
стандартных операторов. Попробуйте найти каких именно.
"""

try:
    N1 = int(input("Input first DEC numeric: "))
    N2 = int(input("Input second DEC numeric: "))

    BIT_OR = N1 | N2
    BIT_AND = N1 & N2
    BIT_XOR = N1 ^ N2
    L_SHIFT = N1 << 2
    R_SHIFT = N1 >> 2

    print(f"Bitwise OR: {bin(BIT_OR)}")
    print(f"Bitwise AND: {bin(BIT_AND)}")
    print(f"Bitwise XOR: {bin(BIT_XOR)}")
    print(f"Bitwise left shift: {bin(L_SHIFT)}")
    print(f"Bitwise right shift: {bin(R_SHIFT)}")

except ValueError:
    print('Incorrect')
