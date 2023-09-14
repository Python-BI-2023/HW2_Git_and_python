def multiply(a,b):
    answer = a * b
    return(answer)
def main():
    a, znak, b = input().split()
    a = float(a)
    b = float(b)
    if znak == "+":
        print(summa(a, b))
    elif znak == "-":
        print(raznost(a, b))
    elif znak == "*":
        print(multiply(a, b))
    elif znak == "/":
        print(delenie(a, b))

