### This will be our great calculator. Please contribute by writing one of the functions
def multiplication(num1, num2): #multiplication of two numbers
    return num1 * num2

def main(): #accepts input, transmits to corresponding function and returns answer 
    my_string = input()
    num1 = float(my_string.split[0])
    num2 = float(my_string.split[2])
    sign = my_string.split[1]
    if sign == "+":
        ans = plus(num1, num2)
    elif sign == "-":
        ans = minus(num1, num2)
    elif sign == "*":
        ans = multiplication(num1, num2)
    elif sign == "/":
        ans = division(num1, num2)
    return ans
answer = main()
print(answer)
