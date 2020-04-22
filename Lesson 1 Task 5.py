alpha = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}
LETTER_1 = input("Введите первую букву: ")
LETTER_2 = input("Введите вторую букву: ")
VAL_1 = int(alpha.get(LETTER_1))
VAL_2 = int(alpha.get(LETTER_2))
print(f'Номер буквы "{LETTER_1}" в алфавите- {VAL_1}, номер буквы "{LETTER_2}"- {VAL_2}')
if VAL_1 > VAL_2:
    DISTANCE = VAL_1 - VAL_2 - 1
    print(f'Между буквой "{LETTER_1}" и буквой "{LETTER_2}" расположено {DISTANCE} букв(ы).')
else:
    DISTANCE = (abs(VAL_1 - VAL_2) - 1)
    print(f'Между буквой "{LETTER_1}" и буквой "{LETTER_2}" расположено {DISTANCE} букв(ы).')