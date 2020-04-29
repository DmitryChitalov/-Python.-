arr = [[],[],[],[],[]]

id = 1
def sum(arr):
    num = 0
    for i in arr:
        num+=i
    return num

for i in arr:
    print(f"Строка №{id}")
    for j in range(0,4):
        i.append(int(input("Введите число: ")))
    i.append(sum(i))
    id+=1
print(arr)