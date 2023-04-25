#!/usr/bin/env python3

import mathlib
import re

## @file core.py
# @brief This file is a parser, returns result of equation
# @author Jakub Pogadl
# @date 21.4 2023
# @return result of equation

# @param separators the definition for a parameter whic seperates the strings from each other
separators = r"([+\-*/^√!]|ln)"

## @brief Checks if the first element in the given equation list is a special number.
# @param equation_list List of equation elements.
# @return Returns 1 if the first element is "5318008", otherwise 0.
def easteregg(equation_list):
    if equation_list[0] == "5318008":
        return 1
    else:
        return 0

## @brief Evaluates a list of equation elements and returns the result.
# @param equation_list List of equation elements.
# @return Returns the evaluated result of the equation.
def return_result(equation_list):
    try:
        if (easteregg(equation_list)):
            return "You found the easter egg!"
        #if separator is followed by -
        indexes_to_remove = []
        for i in range(len(equation_list) - 1):
            if re.match(r'^{}$'.format(separators), equation_list[i]) and equation_list[i+1] == '-':
                equation_list[i+2] = '-' + str(equation_list[i+2])
                indexes_to_remove.append(i+1)

        #remove unnecessary '-' 
        equation_list = [item for i, item in enumerate(equation_list) if i not in indexes_to_remove]
        if equation_list[0] == '--':
            equation_list.pop(0)
        #go through sqrt
        while ("√" in equation_list):
            for i, operator in enumerate(equation_list):
                if operator == "√":
                    result = mathlib.nthroot(float(equation_list[i+1]), float(equation_list[i-1]))
                    equation_list.pop(i-1)
                    equation_list.pop(i-1)
                    equation_list[i-1] = result
        #go through ^
        while ("^" in equation_list):
            for i, operator in enumerate(equation_list):
                if operator == "^":
                    result = mathlib.pwr(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.pop(i-1)
                    equation_list.pop(i)
                    equation_list[i-1] = result

        #go through factorial
        while ("!" in equation_list):
            for i, operator in enumerate(equation_list):
                if operator == "!":
                    result = mathlib.fact(int(equation_list[i-1]))
                    equation_list.pop(i)
                    equation_list[i-1] = result
        
        #go through ln
        while ("ln" in equation_list):
            for i, operator in enumerate(equation_list):
                if not re.search(separators, equation_list[i]): 
                    return "error"
                if operator == "ln":
                    result = mathlib.ln(float(equation_list[i+1]))
                    equation_list[i+1] = result
                    equation_list.pop(i)

        #go through * and /
        while ("*" in equation_list) or ("/" in equation_list):
            for i, operator in enumerate(equation_list):
                if operator == "*":
                    result = mathlib.mul(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.pop(i-1)
                    equation_list.pop(i)
                    equation_list[i-1] = result

                if operator == "/":
                    result = mathlib.div(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.pop(i-1)
                    equation_list.pop(i)
                    equation_list[i-1] = result
        while ("-" in equation_list):
            for i, operator in enumerate(equation_list):
                if operator == "-":
                    result = mathlib.sub(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.pop(i-1)
                    equation_list.pop(i)
                    equation_list[i-1] = result
        #go through add and sub 
        while ("+" in equation_list):
            for i, operator in enumerate(equation_list):
                if operator == "+":
                    result = mathlib.add(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.pop(i-1)
                    equation_list.pop(i)
                    equation_list[i-1] = result
    except:
        return "error"
    return equation_list[0]
## End of file core.py ##