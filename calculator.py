def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b
  
def additional(a, b):
    return a + b
 
def main():
    expression = input("Введите математическое выражение: ")
    number1, operator, number2 = expression.split()
    number1 = float(number1)
    number2 = float(number2)
    result = None
    if operator == "+":
        result = add(number1, number2)
    elif operator == "-":
        result = subtract(number1, number2)
    elif operator == "*":
        result = multiply(number1, number2)
    elif operator == "/":
        result = divide(number1, number2)
    else:
        print("Неверный оператор")
        return
    print(f"Результат: {result:.2f}")
main()



