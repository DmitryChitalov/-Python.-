def sum(n):
    iterator = 1
    num = 0
    for i in range(n):
        if i%2 == 0:
            num+=iterator
            iterator = iterator/2
        else:
            num -= iterator
            iterator = iterator / 2
    return num




if __name__ == "__main__":
    print(f"Ваше число: {sum(int(input('Введите число: ')))}")