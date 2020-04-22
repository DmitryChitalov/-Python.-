YEAR = int(input("Введите год: "))
if YEAR % 4 == 0 and YEAR % 4 != 0 or YEAR % 400 == 0:
    print("Год високосный")
else:
    print("Год не високосный")