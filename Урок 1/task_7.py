A = int(input("a = "))
B = int(input("b = "))
C = int(input("c = "))

if A + B <= C or A + C <= B or B + C <= A:
    print("Треугольник не существует")
elif A != B and A != C and B != C:
    print("Разносторонний")
elif A == B == C:
    print("Равносторонний")
else:
    print("Равнобедренный")
input("Press any to exit...")