#!/usr/bin/env python3

import tkinter
from tkinter import *
from tkinter import messagebox
import re
import mathlib

## \file CountOnMeGUI.py
# \brief GUI calculator that performs basic arithmetic operations as well as root, exponentiation, factorial, ...
#
# This file contains a GUI calculator with a basic interface that allows the user to perform the following operations: addition, subtraction, multiplication, division, exponentiation, root, factorial, and so on.

#generating and configuring window
root = Tk()
root.title("CountOnMe")
#root.iconbitmap("/home/boriss/Documents/VUT-FIT/IVS/proj2/CountOnMe/icon.ico")
root.geometry("570x470+100+100")
root.resizable(False, False)
root.configure(bg="#17161b")

#variable for equation
equation = ""
equation_list = []
separators = r"([+\-*/^√!]|ln)"
ERRORMESSAGE = "error"

## \brief Function that converts equation to list
#
# This function takes the equation string and converts it to a list of numbers and operators.

def convert_equation():
    global equation_list
    global equation
    global seperators

    #if return is pressed when no input was given do nothing
    if equation == "":
        equation_list.append("")
        return
    equation_list = re.split(separators, equation)
    for item in equation_list:
        if item == '':
            equation_list.remove(item)
    #if - is at the beginning of equation
    if equation_list[0] == '-':
        equation_list[1] = '-' + equation_list[1]
        equation_list.remove(equation_list[0])
    #if + is at the beginning of equation
    if equation_list[0] == '+':
        equation_list.remove(equation_list[0])      

    print("Equation list = ", equation_list)

## \brief Function that displays the numbers on the calculator's display
#  
#  This function updates the value of the equation string with the value of the button that was clicked, and displays it on the calculator's display. 
#
#  \param value the value of the button that was clicked

def show(value):
    global equation
    #if error message is on the display first clear it
    if equation == ERRORMESSAGE:
        clear()
    equation += value
    display.config(text = equation)

## \brief Function that displays a message if the user types in a specific string
#  
#  This function checks whether the user has typed in a specific string and displays a message on the calculator's display if they have.
#
#  \return 1 if the user has found the easter egg, 0 otherwise

def easteregg():
    global equation
    if equation == "5318008":
        display.config(text = "You found the easter egg!")
        return 1
    else:
        return 0

## \brief Function that removes the last character from the equation string
#  
#  This function removes the last character from the equation string and updates the value of the calculator's display. 
#

def remove():
    global equation
    if equation == ERRORMESSAGE:
        clear()
    else:
        equation = equation[:-1]
        display.config(text = equation)


## \brief Function that clears the display and resets 'equation' to an empty string
#
#
#

def clear():
    global equation
    equation = ""
    display.config(text = equation)

## \brief The function 'calculate' performs the calculation based on 'equation'
#
# This function calculates and shows the result on the display after hitting '='.
#

def calculate():
    global equation_list
    global separators
    global equation
    result = ""
    
    #go through sqrt
    if(easteregg()):
        return
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

    result = equation_list[0]
    equation = str(equation_list[0])
    display.config(text=result)
    equation_list.clear()

#generating a window for equation/resuglt
display = Label(root, width = 25, height = 2, text = "", font = ("arial", 30))
display.pack()

#help message for user
help_message = ["This is a simple calculator made by our team\n\n",
                "C    -   clears the display\n",
                "⌫  -   removes the last \n          character\n",
                "√    -   root - first type degree \n          of root, then press\n          symbol √ and then type\n          the number you want to\n          root (e.g. 3√8)\n",
                "x!   -   factorial - type the\n          number and then press !\n          (e.g. 3!)\n",
                "xʸ   -   power - type the\n          number, then press xʸ\n          and then type the power\n          (e.g. 2xʸ3)\n",
                "+/- -   negation - changes the\n          sign of the number\n",
                "/    -   division\n",
                "*    -   multiplication\n",
                "-    -   subtraction\n",
                "+   -   addition\n",
                "=   -   calculates the result\n"]

# create a menubar
menubar = Menu(root, bg="#17161b", relief=FLAT, fg= "#fff", bd=0)
# add a Help menu to the menubar
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="Help", command=lambda: messagebox.showinfo("Help", "".join(help_message)))
menubar.add_cascade(label="Help", menu=help_menu)

# display the menubar
root.config(menu=menubar)

#making and configuring buttons
Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#289cbf", command=lambda: clear()).place(x=8, y=100)
Button(root, text="⌫", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#31BED7", command=lambda: remove()).place(x=141, y=100)
Button(root, text="x!", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("!")).place(x=281, y=100)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("/")).place(x=421, y=100)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*")).place(x=421, y=160)

Button(root, text="xʸ", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("^")).place(x=8, y=160)
Button(root, text="ˣ√y", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("√")).place(x=141, y=160)
Button(root, text="ln", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("ln")).place(x=281, y=160)

Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("7")).place(x=8, y=220)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8")).place(x=141, y=220)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9")).place(x=281, y=220)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("-")).place(x=421, y=220)

Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("4")).place(x=8, y=280)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5")).place(x=141, y=280)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6")).place(x=281, y=280)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("+")).place(x=421, y=280)

Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("1")).place(x=8, y=340)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2")).place(x=141, y=340)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3")).place(x=281, y=340)
Button(root, text="0", width=12, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0")).place(x=8, y=400)

Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(".")).place(x=281, y=400)
Button(root, text="=", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#F7A32A", command=lambda: [convert_equation() ,calculate()]).place(x=421, y=340)

#binding keys from keybord
root.bind('1', lambda event: show("1"))
root.bind('2', lambda event: show("2"))
root.bind('3', lambda event: show("3"))
root.bind('4', lambda event: show("4"))
root.bind('5', lambda event: show("5"))
root.bind('6', lambda event: show("6"))
root.bind('7', lambda event: show("7"))
root.bind('8', lambda event: show("8"))
root.bind('9', lambda event: show("9"))
root.bind('0', lambda event: show("0"))
root.bind('.', lambda event: show("."))

root.bind('*', lambda event: show("*"))
root.bind('/', lambda event: show("/"))
root.bind('-', lambda event: show("-"))
root.bind('+', lambda event: show("+"))
root.bind('c', lambda event: clear())
root.bind('<Return>', lambda event: [convert_equation(), calculate()])
root.bind('<BackSpace>', lambda event: remove())



root.mainloop()