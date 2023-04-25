#!/usr/bin/env python3

import math

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
        raise ValueError("Can't take log of negative number!")
    result = math.log(a, math.e)
    return str(round(result, 6))