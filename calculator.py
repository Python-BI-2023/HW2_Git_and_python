"""
It's a calculator tool.
"""


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2



def multiplication(num1, num2):
    return num1 * num2

OPERATIONS = {
    '+': addition,
    '-': subtraction,
    '*': multiplication}
# '/' : division,
# ':' : division


def main():
    input_ = input('Введите математическую операцию: \n').split()
    num1 = float(input_[0])
    num2 = float(input_[2])
    operator = input_[1]
    result = OPERATIONS[operator](num1, num2)
    print(result)


main()
