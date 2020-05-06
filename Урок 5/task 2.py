a = input("Введите первое 16 число: ")
b = input("Введите второе 16 число: ")

list_a = []
list_b = []

for i in a:
    list_a.append(i)
for i in b:
    list_b.append(i)

while len(list_a) != len(list_b):
    if len(list_a) > len(list_b):
        list_b.append('0')
    elif len(list_a) < len(list_b):
        list_a.append('0')

list_a.reverse()
list_b.reverse()

sum = 0
for i in range(len(list_a)):
    sum += int(list_a[i], 16) * pow(16, i)
    sum += int(list_b[i], 16) * pow(16, i)

mult = 0
for i in range(len(list_a)):
    for j in range(len(list_b)):
        mult += (int(list_a[i], 16) * pow(16, i)) * (int(list_b[j], 16) * pow(16, j))

list_a.reverse()
list_b.reverse()


def parse(num):
    list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", 'D', "E", 'F']
    str = ''
    while num > 0:
        str = list[num % 16] + str
        num = num // 16
    return str


print(f"Первое число: {list_a}")
print(f"Второк число: {list_b}")
print(f"Сума {parse(sum)} в 16 системе")
print(f"Сума {sum} в 10 системе")
print(f"Произведение {mult} в 10 системе")
print(f"Произведение {parse(mult)} в 16 системе")