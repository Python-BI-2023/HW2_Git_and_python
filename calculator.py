"""
It's a calculator tool.
"""


def addition(num1, num2):
    """
       Add two numbers.

       Args:
           num1: The first number to add.
           num2: The second number to add.

       Returns:
           The sum of the two numbers.
       """

    return num1 + num2


def subtraction(num1, num2):
    """
        Subtract two numbers.

        Args:
            num1: The first number to subtract.
            num2: The second number to subtract.

        Returns:
            The difference of the two numbers.
        """

    return num1 - num2


def multiplication(num1, num2):
    """
        Multiply two numbers.

        Args:
            num1: The first number to multiply.
            num2: The second number to multiply.

        Returns:
            The product of the two numbers.
        """

    return num1 * num2


def division(num1, num2):
    """
       Divide two numbers.

       Args:
           num1: The dividend.
           num2: The divisor.

       Returns:
           The quotient of the two numbers.
       """
    try:
        return num1 / num2
    except ZeroDivisionError:
        raise ZeroDivisionError("Ooops! calculator.py сan't divide by zero. We will definitely add this feature later")


OPERATIONS = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division,
    ':': division
}


def main():
    """
    Computes the result of a mathematical operation.
    Input is a string containing a mathematical operation.
        The operation must be in the format "number operator number".
    Args:
        No args.
    Returns:
        the result of the mathematical operation.
    """
    input_ = input('Введите математическую операцию: \n').split()
    num1 = float(input_[0])
    num2 = float(input_[2])
    operator = input_[1]
    try:
        result = OPERATIONS[operator](num1, num2)
    except KeyError:
        raise KeyError(f'Unexpected operator {operator}. Supported only +, -, /, :, *')
    print(result)


main()
