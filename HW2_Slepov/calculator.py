def multiplication(b):
    a1 = float(b[0])
    a2 = float(b[2])
    return a1*a2
def addition(b):
    a1 = float(b[0])
    a2 = float(b[2])
    return a1+a2
def substraction(b):
    a1 = float(b[0])
    a2 = float(b[2])
    return a1-a2
def division(b):
    a1 = float(b[0])
    a2 = float(b[2])
    return a1/a2
def main(b):
    if b[1]=="*":
        print(multiplication(b))
    elif b[1]=="+":
        print(addition(b))
    elif b[1]=="/":
        if b[2]==0:
            print("Division by 0 is FALSE")
        else:
            print(division(b))
    elif b[1]=="-":
        print(substraction(b))
    else:
        print("Enter correct form of operation")

a = input()
b = a.split()
main(b)

