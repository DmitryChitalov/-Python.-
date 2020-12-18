# По введенным пользователем координатам двух точек вывести уравнение прямой вида
# y = kx + b, проходящей через эти точки.

print('Plese provide coordinates for a(x1;y1):')
x1 = float(input('\tx1 = '))
y1 = float(input('\ty1 = '))
 
print('Plese provide coordinates for b(x2;y2):')
x2 = float(input('\tx2 = '))
y2 = float(input('\ty2 = '))
 
k = (y1 - y2) / (x1 - x2)
b = y2 - k*x2
print(f'Formula of the line through points: a({x1};{y1}) and b({x2};{y2})')
print(' y = %.2f*x + %.2f' % (k, b))