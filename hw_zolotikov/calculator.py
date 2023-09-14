def mysum(a, b):
    return a+b
def mydiv(x,y):
    return x/y
def main():
    inp = input('vvedite to, chto nado poschitat')
    inp = inp.split(sep =' ')
    x = float(inp[0])
    y = float(inp[2])
    sign = inp[1]
    result = 0
    if sign == "+":
        result = mysum(x,y)
    elif sign == "-":
        result = mysub(x,y)
    elif sign == "*":
        result = mymult(x,y)
    elif sign == "/":
        result = mydiv(x,y)
    else:
        result = "Oshibka"
    print(result)
main()
