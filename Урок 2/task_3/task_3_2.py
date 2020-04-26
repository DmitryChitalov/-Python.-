def rev(num, rev_num):
    if num <= 0:
        print(f"Число наооборот: {rev_num}")
        return 
    rev(num // 10, rev_num * 10 + num % 10)


if __name__ == "__main__":
   rev(int(input('Введите число: ')), 0)