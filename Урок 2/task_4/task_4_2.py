def sum(num, n, i):
    if n <=0:
        print(num)
    elif n%2 == 0:
        num+=i
        sum(num, n-1, i/2)
    else:
        num -= i
        sum(num, n - 1, i / 2)



if __name__ == "__main__":
    sum(0, int(input('Введите число: ')), 1)
    #sum(начальное число, количсество, от какого числа делим на 2)