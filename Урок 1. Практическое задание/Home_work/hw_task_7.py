a = int(input())
b = int(input())
c = int(input())

if a + b <= c or a + c <= b or b + c <= a:
    print('Такого быть не может...')
elif a == b == c:
    print('Равносторонний')
elif a != b and a != c and b != c:
    print('Разносторонний')
else:
    print("Равнобедренный")
