#!/usr/local/bin/python3


"""
Задание 2. Выполнить логические побитовые операции "И", "ИЛИ"
и др. над числами 5 и 6. Выполнить
над числом 5 побитовый сдвиг вправо и влево на два знака.
Подсказка: это стандартные операции, которые осуществляются с помощью
стандартных операторов. Попробуйте найти каких именно.
"""

visual_delimiter = '*************'
print('Логическое и')
print(5 & 6)
print(bin(5))
print(bin(6))
print(bin(5 & 7))
print(visual_delimiter)

print('Логическое или')
print(5 | 6)
print(bin(5))
print(bin(6))
print(bin(5 | 6))
print(visual_delimiter)

print('Исключительное или')
print(5 ^ 6)
print(bin(5))
print(bin(6))
print(bin(5 ^ 6))
print(visual_delimiter)

print('Побитовое не')
print(~ 5)
print(bin(~ 5))
print(bin(5))
print(bin(6))
print(~ 6)
print(bin(~ 6))
print(visual_delimiter)

print('Побитовый сдвиг числа вправо')
print(5 >> 2)
print(bin(5))
print(bin(6))
print(bin(5 >> 2))
print(visual_delimiter)

print('Побитовый сдвиг числа влево')
print(5 << 2)
print(bin(5))
print(bin(6))
print(bin(5 << 2))
print(visual_delimiter)

# Не до конца понел зачем эти операцыи