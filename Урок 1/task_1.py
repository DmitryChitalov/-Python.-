NUM = input("Enter NUM: ")
SUM = 0
MUL = 1
for i in NUM:
    SUM += float(i)
    MUL *= float(i)

print(SUM)
print(MUL)
input("Press any to exit...")