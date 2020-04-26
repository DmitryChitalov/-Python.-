def count(num):
    if num <= 0:
        print("Число не натуральное")
    even = 0
    odd = 0
    while num > 0:
        if num%2 == 0:
            even+=1
        else:
            odd+=1
        num = int(num/10)
    print(f"Четных: {even}")
    print(f"Нечетных: {odd}")

if __name__ == "__main__":
    count(int(input("Введите натуральное число: ")))