def count(num, even, odd):
    if num <=0:
        print(f"Четных: {even}")
        print(f"Нечетных: {odd}")
        return
    if num%2 == 0:
        count(int(num/10), even+1, odd)
    else:
        count(int(num / 10), even, odd+1)



if __name__ == "__main__":
    count(int(input("Введите натуральное число: ")), 0, 0)