def multiplication(a,b):
    answer = a * b
    return answer

def summing (a, b):
    return a + b

expression = input ("Введите выражение вида 1 + 1 ")
nums = expression.split()
num1 = float(nums[0])
operator = nums[1]
num2 = float(nums[2])
if operator == '+':
    result = summing(num1, num2)
print (result)
