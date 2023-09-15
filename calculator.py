def multiply(a,b):
    return a*b

def subtraction(a, b):
    return a - b 

def calc_parser(calc_string):
    calc_list = calc_string.split(' ')
    calc_list[0] = float(calc_list[0])
    calc_list[2] = float(calc_list[0])
    return calc_list

calc_string = input('Enter your expression:')
command = calc_parser(calc_string)[1]

while calc_string != 'exit':
    if command in calculator_func_dict:
        print(calculator_func_dict[command](calc_string[0], calc_string[2]))
    else:
        print('Seems like an invalid expression. Please, enter valid expression!')

    calc_string = input('Enter your expression:')
    command = calc_parser(calc_string)[1]

print('See you next time!')