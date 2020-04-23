NUM = int(input("Введите номер между 1-26: "))
if NUM > 26 or NUM <= 0:
    print("Ввели не тот диапазон")
else:
    print(chr(NUM + ord("a") - 1))
input("Press any to exit...")