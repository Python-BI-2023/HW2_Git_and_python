'''
It's a calculator tool.
'''

OPERATIONS = {
    '+' : addition(num1, num2),
    '-' : subtraction,
    '*' : multiplication,
    '/' : division,
    ':' : division
}


def main():
    input_ = input('Введите математическую операцию').split()
    num1 = float(input_[0])
    num2 = float(input_[2])
    operator = input_[1]
    result = 0

    OPERATIONS[operator]
    print(result)