x1_val = int(input('Enter the coordinate '
                   'of the 1st point along the x axis: '))
y1_val = int(input('Enter the coordinate '
                   'of the 1st point along the y axis: '))
x2_val = int(input('Enter the coordinate '
                   'of the 2nd point along the x axis: '))
y2_val = int(input('Enter the coordinate '
                   'of the 2nd point along the x axis: '))

a = (y1_val - y2_val)
b = (x2_val - x1_val)
c = (x1_val * y2_val - x2_val * y1_val)

a_tmp = (-a) / b
c_tmp = (-c) / b

print(f'y = {a_tmp} * x + {c_tmp}')
