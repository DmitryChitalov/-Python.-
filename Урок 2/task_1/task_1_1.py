def math(a, b, sign):
    if sign == "*":
        return (a*b)
    elif sign == "/":
        if b == 0:
            return "Деление на 0"
        else:
            return a/b
    elif sign == "+":
        return a+b
    elif sign == "-":
        return a-b
    else:
        return "Неверный ввод знака действий"




if __name__ == "__main__":
    while True:
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
        sign = input("Введите знак(*, /, -, +) 0 для выхода: ")
        if sign == "0":
            exit(0)
        print(f"Ваш ответ = {math(a, b, sign)}")
