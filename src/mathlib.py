#!/usr/bin/env python3

def add(a,b):
    result = a + b
    return str(round(result, 6))

def sub(a,b):
    result = a - b
    return str(round(result, 6)) 

def div(a,b):
    if b == 0:
        raise ZeroDivisionError("Can't divide by zero!")
    result = a / b
    return str(round(result, 6))

def mul(a,b):
    result = a * b
    return str(round(result, 6))

def nthroot(a, b):
    if b == 0:
        raise ZeroDivisionError("Can't divide by zero!")
    if a < 0 and b % 2 == 0:
        raise ValueError("Result is not a real number!")
    result = a**(1/b)
    return str(round(result, 6))

def fact(a):
    if a < 0:
        raise ValueError("Can't take factorial of negative number!")
    fact = 1
    for num in range(2, a + 1):
        fact *= num
    return str(fact)

def pwr(a,b):
    result = a**b
    return str(round(result, 6))

def ln(a):
	if a <= 0:
		raise ValueError("Can't take ln of negative number!")
	n = 1000000.0
	return round(n * ((a ** (1/n)) - 1), 6)
    
