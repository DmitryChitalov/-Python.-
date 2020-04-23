POINT_X1 = float(input("Enter A(x): "))
POINT_Y1 = float(input("Enter A(y): "))
POINT_X2 = float(input("Enter B(x): "))
POINT_Y2 = float(input("Enter B(y): "))

K = (POINT_Y1 - POINT_Y2) / (POINT_X1 - POINT_X2)
B = POINT_Y2 - K * POINT_X2
print(" y = %.2f*x + %.2f" % (K, B))
input("Press any to exit...")
