x1 = float(input('x_1 = '))
y1 = float(input('y_1 = '))

x2 = float(input('x_2 = '))
y2 = float(input('y_2 = '))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print(f" y = {k} * x + {b}")