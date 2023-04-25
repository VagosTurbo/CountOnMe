#!/usr/bin/env python3

import mathlib
import re

separators = r"([+\-*/^√!]|ln)"


def return_result(equation_list):
    result = ""
    #go through sqrt
    try: 
        while ("√" in equation_list):
            for i, operator in enumerate(equation_list):
                print(equation_list)
                if operator == "√":
                    result = mathlib.nthroot(float(equation_list[i+1]), float(equation_list[i-1]))
                    equation_list.remove(equation_list[i-1])
                    equation_list.remove(equation_list[i])
                    equation_list[i-1] = result
                    print(equation_list)
        #go through ^
        while ("^" in equation_list):
            for i, operator in enumerate(equation_list):
                print(equation_list)
                if operator == "^":
                    result = mathlib.pwr(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.remove(equation_list[i-1])
                    equation_list.remove(equation_list[i])
                    equation_list[i-1] = result
                    print(equation_list)
        #go through factorial
        while ("!" in equation_list):
            for i, operator in enumerate(equation_list):
                if operator == "!":
                    result = mathlib.fact(int(equation_list[i-1]))
                    equation_list.remove(equation_list[i])
                    equation_list[i-1] = result
                    print(equation_list)

        #if separator is followed by -
        indexes_to_remove = []
        for i in range(len(equation_list) - 1):
            if re.match(separators, equation_list[i]) and equation_list[i+1] == '-':
                print("equation_list[i+2] = ", equation_list[i+2])
                equation_list[i+2] = '-' + str(equation_list[i+2])
                print("Zmenene equation_list[i+2] = ", equation_list[i+2])
                indexes_to_remove.append(i+1)
                print("indexes_to_remove", indexes_to_remove)
        #remove unnecessary '-'
        equation_list = [item for i, item in enumerate(equation_list) if i not in indexes_to_remove]  

        #go through ln
        while ("ln" in equation_list):
            for i, operator in enumerate(equation_list):
                print(equation_list)
                if operator == "ln":
                    result = mathlib.ln(float(equation_list[i+1]))
                    equation_list[i+1] = result
                    equation_list.remove(equation_list[i])
                    print(equation_list)
            
        #go through * and /
        while ("*" in equation_list) or ("/" in equation_list):
            for i, operator in enumerate(equation_list):
                print(equation_list)
                if operator == "*":
                    result = mathlib.mul(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.remove(equation_list[i-1])
                    equation_list.remove(equation_list[i])
                    equation_list[i-1] = result
                    print(equation_list)
                if operator == "/":
                    result = mathlib.div(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.remove(equation_list[i-1])
                    equation_list.remove(equation_list[i])
                    equation_list[i-1] = result
                    print(equation_list)

        #go through add and sub 
        while ("+" in equation_list) or ("-" in equation_list):
            for i, operator in enumerate(equation_list):
                print(equation_list)
                if operator == "-":
                    result = mathlib.sub(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.remove(equation_list[i-1])
                    equation_list.remove(equation_list[i])
                    equation_list[i-1] = result
                    print(equation_list)

                if operator == "+":
                    result = mathlib.add(float(equation_list[i-1]), float(equation_list[i+1]))
                    equation_list.remove(equation_list[i-1])
                    equation_list.remove(equation_list[i])
                    equation_list[i-1] = result
                    print(equation_list)
    except:
        return "error"
    return equation_list[0]