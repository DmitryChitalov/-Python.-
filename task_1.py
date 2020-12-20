# Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. 
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. 
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. 
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. 
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

# Я преписал это как калькулятор.
# Извините 
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def checkinput(inpstr):
    math_sins = '+' '-' '*' '/'
    num1, sign, num2 = inpstr.split(' ')
    result = True
    if not is_number(num1):
        print(f'{num1} is not number')
        result = False    
    if not is_number(num2):
        print(f'{num2} is not number')
        result = False    
    if math_sins.find(sign) == -1:
        print(f'{sign} is not allowed math operator.')
        result = False
    return result         

def math_op(inpstr):
    result = ''
    num1, sign, num2 = inpstr.split(' ')
    num1 = float(num1)
    num2 = float(num2)
    if sign == '+':
        result = str(num1 + num2)
    elif sign == '-':
        result = str(num1 - num2)
    elif sign == '*':
        result = str(num1 * num2)
    elif sign == '/':
        if num2 != 0:
            result = str(num1 / num2)
        else:
            result = 'N/A trying to divide by 0'
    return result            

 

while True:
    print('Please provide what you want to do. Fo instance "12 + 25 = <Enter>" : ')
    inp_str = input('Number and signs please split by space. For cancell type "q" ').lstrip().rstrip()
    if inp_str == 'q':
        break
    if inp_str.count(' ') != 2:
        print('Error. Your provided not 3 values')
        break
    if checkinput(inp_str):
        print(f'The result {inp_str} = {math_op(inp_str)}')
