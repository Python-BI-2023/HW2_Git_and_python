def divide(a, b):
  return a/b

def add(a,b):
    return a+b

def multiply(x,y):
    return(x*y)
  
def subtract(eq1,eq2):
	return(eq1-eq2)

def main():
#   eq = [int(i) if i.isdigit() else i for i in input().split()]
    eq = input().split()
    match eq[1]:
        case "+":
            return add(int(eq[0]), int(eq[2]))
        case "-":
            return subtract(int(eq[0]), int(eq[2]))
        case "*":
            return multiply(int(eq[0]), int(eq[2]))
        case "/":
            return divide(int(eq[0]), int(eq[2]))
main()
