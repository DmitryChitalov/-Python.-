def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum+=i
    if sum == n * (n + 1) // 2:
        print("Доказано")
    else:
        print("Не доказано")
    print(sum)
    print(n * (n + 1) // 2)


if __name__ == "__main__":
    sum(int(input("Введите число: ")))