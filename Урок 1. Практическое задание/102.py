"""
Не понял ремарку задания "объясните результат",
Прикладываю псевдотаблицы с логическими операциями.
+-and-+ +--or--+ +-xor-+
|--+--| |--+---| |--+--|
|00| 0| |00| 0 | |00| 0|
|01| 0| |01| 1 | |01| 1|
|10| 0| |10| 1 | |10| 1|
|11| 1| |11| 1 | |11| 0|
+-----+ +------+ +-----+
5 и 6 по битам 0101 и 0110 соотвественно.

Сдвиг вправо удаляет n бит.
Сдвиг влево дописывает n нулей.
"""

number_a = 5
number_b = 6

or_bit = number_a | number_b
xor_bit = number_a ^ number_b
and_bit = number_a & number_b

print(f'Logical bitwise "AND" result: {bin(and_bit)}')
print(f'Logical bitwise "OR" result: {bin(or_bit)}')
print(f'Logical bitwise "XOR" result: {bin(xor_bit)}')

tmp = number_a << 2
tmp_2 = number_a >> 2

print(tmp, tmp_2)

