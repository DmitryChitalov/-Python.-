# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, 
# составленного из этих отрезков. Если такой треугольник существует, то определить, 
# является ли он разносторонним, равнобедренным или равносторонним.

print('Plese provide lengths sides of triangle:')
l1 = float(input('\tl1 = '))
l2 = float(input('\tl2 = '))
l3 = float(input('\tl3 = '))
 
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2 :
    print (f'It is possible to create triangle from provided sides')
    if l1 != l2 and l2 != l3 and l3 != l1 :
        print(f'Here is an scalene triangle')
    elif l1 == l2 and l2 == l3 and l3 == l1 :
        print(f'Here is an equilateral triangle')
    elif l1 == l2  or l1 == l3 or l2 == l3 :
        print(f'Here is an isosceles triangle')
else:
    print (f'It is impossible to create triangle from provided sides')
