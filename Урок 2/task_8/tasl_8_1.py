def count(num, i):
    times = 0
    while num > 0:
        if i == num%10:
            times+=1
        num = num // 10
    return times



if __name__ == "__main__":
    size = int(input("Сколько будет чисел: "))
    i = int(input("Какую цифру ищем: "))
    d = 0
    while size > 0:
        d+= count(int(input("Введите число: ")), i)
        size-=1
    print(f"Было введено {d} цифр '{i}'")