"""
Задание 2. Выполнить логические побитовые операции "И", "ИЛИ"
и др. над числами 5 и 6. Выполнить
над числом 5 побитовый сдвиг вправо и влево на два знака.

Подсказка: это стандартные операции, которые осуществляются с помощью
стандартных операторов. Попробуйте найти каких именно.
"""

A = 5
B = 6
N = 2
print(f'5 = {bin(A)}\t6 = {bin(B)}')
print('---------------------------------------')
print(f"ИЛИ \t\t{A} | {B}\t{A | B}\t{bin(A | B)}")
print(f" И \t\t\t{A} & {B}\t{A & B}\t{bin(A & B)}")
print(f"Искл ИЛИ \t{A} ^ {B}\t{A ^ B}\t{bin(A ^ B)}")
print('---------------------------------------')
print(f"Побитовый сдвиг в право \t{A} >> {N}\t{A >> N}\t{bin(A >> N)}")
print(f"Побитовый сдвиг в лево \t\t{A} << {N}\t{A << N}\t{bin(A << N)}")
