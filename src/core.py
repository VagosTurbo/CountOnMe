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
    try:

        if (easteregg(equation_list)):
            return "You found the easter egg!"


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
                print(equation_list)
                if operator == "√":
                    result = mathlib.nthroot(float(equation_list[i+1]), float(equation_list[i-1]))
                    equation_list.remove(equation_list[i-1])
                    equation_list.remove(equation_list[i])
                    equation_list[i-1] = result
        #go through ^
        while ("^" in equation_list):
            for i, operator in enumerate(equation_list):
                if operator == "^":
                    result = mathlib.pwr(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.remove(equation_list[i-1])
                    equation_list.remove(equation_list[i])
                    equation_list[i-1] = result
        #go through factorial
        while ("!" in equation_list):
            for i, operator in enumerate(equation_list):
                if operator == "!":
                    result = mathlib.fact(int(equation_list[i-1]))
                    equation_list.remove(equation_list[i])
                    equation_list[i-1] = result

        #if separator is followed by -
        indexes_to_remove = []
        for i in range(len(equation_list) - 1):
            if re.match(separators, equation_list[i]) and equation_list[i+1] == '-':
                equation_list[i+2] = '-' + str(equation_list[i+2])
                indexes_to_remove.append(i+1)

        #go through ln
        while ("ln" in equation_list):
            for i, operator in enumerate(equation_list):
                if operator == "ln":
                    result = mathlib.ln(float(equation_list[i+1]))
                    equation_list[i+1] = result
                    equation_list.remove(equation_list[i])
            
        #go through * and /
        while ("*" in equation_list) or ("/" in equation_list):
            for i, operator in enumerate(equation_list):
                if operator == "*":
                    result = mathlib.mul(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.remove(equation_list[i-1])
                    equation_list.remove(equation_list[i])
                    equation_list[i-1] = result
                if operator == "/":
                    result = mathlib.div(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.remove(equation_list[i-1])
                    equation_list.remove(equation_list[i])
                    equation_list[i-1] = result

        #go through add and sub 
        while ("+" in equation_list) or ("-" in equation_list):
            for i, operator in enumerate(equation_list):
                print(equation_list)
                if operator == "-":
                    result = mathlib.sub(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.remove(equation_list[i-1])
                    equation_list.remove(equation_list[i])
                    equation_list[i-1] = result
                if operator == "+":
                    result = mathlib.add(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.remove(equation_list[i-1])
                    equation_list.remove(equation_list[i])
                    equation_list[i-1] = result
    except:
        return "error"
    return equation_list[0]