def math():
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    sign = input("Введите знак(*, /, -, +) 0 для выхода: ")

    if sign == "*":
        print(a*b)
    elif sign == "/":
        if b == 0:
            print("Деление на 0")
        else:
            print(a/b)
    elif sign == "+":
        print(a+b)
    elif sign == "-":
        print(a-b)
    elif sign == "0":
        return
    else:
        print("Неверный ввод знака действий")
    math()



if __name__ == "__main__":
    math()
