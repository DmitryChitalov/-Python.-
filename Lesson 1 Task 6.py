ALPH = 'abcdefghijklmnopqrstuvwxyz'
NUM = int(input("Введите номер буквы в диапазоне от 1 до 26: "))
LETTER = ALPH[NUM-1]
print(f'Под номером {NUM} в алфавите находится буква "{LETTER}".')