import math

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    result = a / b
    return str(result)

def mul(a,b):
    result = a * b
    return str(result)

def sqrt(a, b):
    result = a**(1/b)
    return str(result)

def fact(a):
    fact = 1
    for num in range(2, a + 1):
        fact *= num
    return fact

def pwr(a,b):
    result = a**b
    return result

def log(a):
    result = math.log(a)
    return result