def cutter(symb, symb_counter):
    str_line = ' '
    while symb_counter > 0:
        str_line += f'{symb} - {chr(symb)} '
        symb_counter -= 1
        symb += 1
    return print(str_line)


min_symb = 32       # Reassigned parameter
max_symb = 127      # Reassigned parameter
step = 10           # Reassigned parameter

symb_counter = 0
scissors = max_symb - min_symb + 1
counter = 0
symb = min_symb


while symb < max_symb:
    if scissors > step:
        symb_counter = step
    else:
        symb_counter = max_symb - symb + 1
    current_line = cutter(symb, symb_counter)
    symb += step
    scissors -= step
