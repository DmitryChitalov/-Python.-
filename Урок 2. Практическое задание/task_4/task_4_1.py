ttl_elements = int(input('Enter the number of items: '))
tmp = 1
el_sum = 0
while not ttl_elements == 0:
    el_sum += tmp
    tmp = tmp / -2
    ttl_elements -= 1
print(f'The sum of the specified number of elements is equal to: {el_sum}')
