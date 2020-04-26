def rev(num):
    rev_num = 0
    while num>0:
        rev_num = rev_num * 10 + num % 10
        num = num // 10
    return rev_num

if __name__ == "__main__":
    print(f"Число наоборот: {rev(int(input('Введите число: ')))}")