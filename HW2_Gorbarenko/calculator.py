
a,b,c = input().split()
a = int(a)
c = int(c)

if (b == "+"): #sokol_sum
  print(sokol_sum(a,c))
elif (b == "-"): #delta
  print(delta(a,c))
elif (b == "*"): #multi
  print(multi(a,c))
elif (b == "/") : #teilen
  print(teilen(a,c))
else:
  print("I dont know what it is")


def teilen(a,b):
    return(a / b)

def delta(a, b):
    return a - b

def multi(a, b):
    return(a * b)
