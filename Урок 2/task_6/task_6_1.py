from random import random

def guess(num, attempts):
    for i in range(attempts):
        a = int(input("Введите число: "))
        if a == num:
            print("Вы угадали!")
            return
        elif a > num:
            print("Слишком большое")
        else:
            print("Слишком маленькое")
    print("Потратили все попытки")

if __name__ == "__main__":
    rnd = round(random() * 100)
    print(rnd)
    guess(rnd, 10)