#!/usr/bin/env python3

import math

def add(a,b):
    return str(a+b)

def sub(a,b):
    return str(a-b)

def div(a,b):
    if b == 0:
        raise ZeroDivisionError("Can't divide by zero!")
    return str(a/b)

def mul(a,b):
    return str(a*b)

def nthroot(a, b):
    if b == 0:
        raise ZeroDivisionError("Can't divide by zero!")
    return str(a**(1/b))

def fact(a):
    fact = 1
    for num in range(2, a + 1):
        fact *= num
    return str(fact)

def pwr(a,b):
    result = a**b
    return str(result)

def log(a):
    if a <= 0:
        raise ValueError("Can't take log of negative number!")
    result = math.log(a, math.e)
    return str(result)