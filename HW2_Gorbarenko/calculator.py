
a,b,c = input().split()
if ("." in a) or ("." in c):
    a = float(a)
    c = float(c)
elif ("," in a) or ("," in c):
    a = float(a.replace(',','.'))
    c = float(c.replace(',','.'))
else:
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




