def main():
    calc_input = input()
    calc_input_lst = calc_input.split()

    operation = calc_input_lst[1]
    number_1 = calc_input_lst[0]
    number_1 = float(number_1)
    number_2 = calc_input_lst[2]
    number_2 = float(number_2)

    if operation == "+":
        res = addition(number_1, number_2)
    elif operation == "-":
        res = subtraction(number_1, number_2)
    elif operation == "*":
        res = multiplication(number_1, number_2)
    elif operation == "/":
        res = division(number_1, number_2)
    return print(res)


def multiplication(number_1, number_2):
    res = number_1 * number_2
    return res


def subtraction(number_1, number_2):
    res = number_1 - number_2
    return res


def addition(number_1, number_2):
    res = number_1 + number_2
    return res


def division(n1, n2):
    res = n1 / n2
    return res


main()
