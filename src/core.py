#!/usr/bin/env python3

import mathlib
import re

separators = r"([+\-*/^√!]|ln)"

def easteregg(equation_list):
    if equation_list[0] == "5318008":
        return 1
    else:
        return 0
        
def return_result(equation_list):


    if (easteregg(equation_list)):
        return "You found the easter egg!"

    try:
        #if separator is followed by -
        indexes_to_remove = []
        for i in range(len(equation_list) - 1):
            if re.match(separators, equation_list[i]) and equation_list[i+1] == '-':
                equation_list[i+2] = '-' + str(equation_list[i+2])
                indexes_to_remove.append(i+1)
        #remove unnecessary '-'
        equation_list = [item for i, item in enumerate(equation_list) if i not in indexes_to_remove]
        
        #go through sqrt
        while ("√" in equation_list):
            for i, operator in enumerate(equation_list):
                if operator == "√":
                    print("toto je i", i)
                    result = mathlib.nthroot(float(equation_list[i+1]), float(equation_list[i-1]))
                    equation_list.pop(i-1)
                    equation_list.pop(i-1)
                    equation_list[i-1] = result
                    print(equation_list)
        print("opustam odmocninu")
        #go through ^
        while ("^" in equation_list):
            for i, operator in enumerate(equation_list):
                if operator == "^":
                    result = mathlib.pwr(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.pop(i-1)
                    equation_list.pop(i)
                    equation_list[i-1] = result
                    print(equation_list)

        #go through factorial
        while ("!" in equation_list):
            for i, operator in enumerate(equation_list):
                if operator == "!":
                    result = mathlib.fact(int(equation_list[i-1]))
                    equation_list.pop(i)
                    equation_list[i-1] = result
                    print(equation_list)
        
        #go through ln
        while ("ln" in equation_list):
            for i, operator in enumerate(equation_list):
                if operator == "ln":
                    result = mathlib.ln(float(equation_list[i+1]))
                    equation_list[i+1] = result
                    equation_list.pop(i)
                    print(equation_list)

        #go through * and /
        while ("*" in equation_list) or ("/" in equation_list):
            for i, operator in enumerate(equation_list):
                if operator == "*":
                    result = mathlib.mul(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.pop(i-1)
                    equation_list.pop(i)
                    equation_list[i-1] = result
                    print(equation_list)

                if operator == "/":
                    result = mathlib.div(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.pop(i-1)
                    equation_list.pop(i)
                    equation_list[i-1] = result
                    print(equation_list)
        while ("-" in equation_list):
            for i, operator in enumerate(equation_list):
                if operator == "-":
                    result = mathlib.sub(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.pop(i-1)
                    equation_list.pop(i)
                    equation_list[i-1] = result
                    print(equation_list)
        #go through add and sub 
        while ("+" in equation_list):
            for i, operator in enumerate(equation_list):
                if operator == "+":
                    result = mathlib.add(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.pop(i-1)
                    equation_list.pop(i)
                    equation_list[i-1] = result
                    print(equation_list)
    except:
        return "error"

    return equation_list[0]