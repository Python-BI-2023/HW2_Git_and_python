
a,b,c = input().split()
a = int(a)
c = int(c)


def teilen(a,b):
    return(a / b)

def delta(a, b):
    return a - b

def  sokol_sum(a,b):
   return a+b

def multi(a, b):
    return(a * b)


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




