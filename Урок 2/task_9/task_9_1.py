def sum(num):
    sum = 0
    while num > 0:
        sum+=num%10
        num = num//10
    return sum

if __name__ == "__main__":
    size = int(input("Сколько будет чисел: "))
    max = 0
    max_i = 0
    while size > 0:
        i = int(input("Введите число: "))
        num = sum(i)
        max_i = i
        if max < num:
            max = num
        size -= 1
    print(f"Наибольшее число по сумме цифр: {max_i}, сумма его цифр: {max}")
