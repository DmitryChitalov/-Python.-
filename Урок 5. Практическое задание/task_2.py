from collections import defaultdict


def comparison(args):
    len_a = len(args[0])
    len_b = len(args[1])
    if not len_a == len_b:
        while not len_a == len_b:
            if len_a > len_b:
                args[1].insert(0, '0')
                len_b = len(args[1])
            else:
                args[0].insert(0, '0')
                len_a = len(args[0])
    return args


def hex_to_dec(args, hex):
    decihex = []
    for item in args:
        curr = 0
        x = len(args[0]) - 1
        for el in item:
            if el.isalpha():
                curr += int(hex[el][0]) * 16 ** x
                x -= 1
            else:
                curr += int(el[0]) * 16 ** x
                x -= 1
        decihex.append(curr)
    return decihex


def dec_to_hex(num):
    base = '0123456789ABCDEF'
    if num <= 15:
        return base[num]
    return f'{dec_to_hex(num // 16)}{base[num % 16]}'


def solution(args):
    curr_summ = sum(args)
    curr_mul = args[0] * args[1]
    answ_list = list()
    answ_list.append(dec_to_hex(curr_summ))
    answ_list.append(dec_to_hex(curr_mul))
    return answ_list


n = 0
num_list = list()
while not n == 2:
    num_list.append([i for i in
                     input(f'Input {n + 1} nubmer in hex: ')])
    n += 1


hex = [0, 1, 2, 3,
       4, 5, 6, 7, 8,
       9, 'A', 'B', 'C',
       'D', 'E', 'F', 16]
hex_dict = defaultdict(list)
deci = 0


for el in hex:
    hex_dict[el].append(deci)
    deci += 1

while len(num_list) != 2:
    num_list.append(
        [x for x in
         input(f'Enter {len(num_list) + 1} number in hex: ')]
    )

fin = (solution(
    hex_to_dec(
        comparison(num_list), hex_dict)))
print(fin[0])
print(f'{[x for x in fin[0]]}')
print(f'{[x for x in fin[1]]}')
