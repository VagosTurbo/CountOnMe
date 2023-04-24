import tkinter
from tkinter import *
from tkinter import messagebox
import re

#generating and configuring window
root = Tk()
root.title("CountOnMe")
#p1 = PhotoImage(file = 'CountOnMelogo_FINAL.png')
#root.iconphoto(False, p1)
root.geometry("680x570+100+100")
root.resizable(False, False)
root.configure(bg="#17161b")



#clears the display and equation
def clear():
    global equation
    equation = ""
    display.config(text = equation)


def bmi():
    root_bmi = Tk()
    root_bmi.title("BMI")
    root_bmi.resizable(False, False)
    root_bmi.configure(bg="#2a2d36")
    Label(root_bmi, text="Enter your height: ", font=("arial", 20, "bold"), fg="#fff", bg="#2a2d36").grid(row=0, column=0)
    Entry(root_bmi, width=10, font=("arial", 20, "bold"), fg="#fff", bg="#2a2d36").grid(row=0, column=1)
    Label(root_bmi, text="Enter your weight: ", font=("arial", 20, "bold"), fg="#fff", bg="#2a2d36").grid(row=1, column=0)
    Entry(root_bmi, width=10, font=("arial", 20, "bold"), fg="#fff", bg="#2a2d36").grid(row=1, column=1)
    Button(root_bmi, text="Calculate", width=10, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#289cbf").grid(row=2, column=1)
    Label(root_bmi, text="Your BMI is: ", font=("arial", 20, "bold"), fg="#fff", bg="#2a2d36").grid(row=3, column=0)
    Label(root_bmi, text="Your BMI category is: ", font=("arial", 20, "bold"), fg="#fff", bg="#2a2d36").grid(row=4, column=0)
    Label(root_bmi, text="Your ideal weight is: ", font=("arial", 20, "bold"), fg="#fff", bg="#2a2d36").grid(row=5, column=0)
    Entry(root_bmi, text="", font=("arial", 20, "bold"), fg="#fff", bg="#2a2d36").grid(row=3, column=1)
    Entry(root_bmi, text="", font=("arial", 20, "bold"), fg="#fff", bg="#2a2d36").grid(row=4, column=1)
    Entry(root_bmi, text="", font=("arial", 20, "bold"), fg="#fff", bg="#2a2d36").grid(row=5, column=1)
    root_bmi.mainloop()

#creates window for basic stopwatch
def stopwatch():
    root_stopwatch = Tk()
    root_stopwatch.title("Stopwatch")
    root_stopwatch.resizable(False, False)
    root_stopwatch.configure(bg="#2a2d36")
    Label(root_stopwatch, text="00:00:00", font=("arial", 20, "bold"), fg="#fff", bg="#2a2d36").grid(row=0, columnspan=2)
    Button(root_stopwatch, text="Start", width=10, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#289cbf").grid(row=2, column=0)
    Button(root_stopwatch, text="Stop", width=10, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="#289cbf").grid(row=2, column=1)
    root_stopwatch.mainloop()




#generating a window for equation/result
display = Label(root, width = 30, height = 4, text = "", font = ("arial", 30))
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
menubar.add_command(label="Help", command=lambda: messagebox.showinfo("Help", "".join(help_message)))

# add a Modes menu to the menubar
modes = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Modes", menu = modes)
modes.add_command(label="Standard - basic calculator", command=lambda: messagebox.showinfo("Modes", "There are 3 modes in this calculator:\n\n1. Standard - basic calculator\n2. Scientific - advanced calculator\n3. Programmer - binary calculator"))
modes.add_command(label="Scientific - advanced calculator")
modes.add_command(label="Programmer - binary calculator")

# add a Special menu to the menubar
special = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Special", menu = special)
special.add_command(label="BMI  -  Body Mass Index",  command=lambda: bmi())
special.add_command(label="Stopwatch", command=lambda: stopwatch())
special.add_command(label="Currency converter")

# display the menubar
root.config(menu=menubar)

#making and configuring buttons

Button(root, text="C", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#289cbf", command=lambda: clear()).place(x=8, y=200)
Button(root, text="⌫", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#31BED7", command=lambda: clear()).place(x=121, y=200)
Button(root, text="ln", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=231, y=200)
Button(root, text="x!", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=341, y=200)
Button(root, text="f(x)", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=451, y=200)
Button(root, text="/", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=561, y=200)

Button(root, text="xʸ", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=8, y=260)
Button(root, text="ˣ√y", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=121, y=260)
Button(root, text="(", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=231, y=260)
Button(root, text=")", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=341, y=260)
Button(root, text="<", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=451, y=260)
Button(root, text="*", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=561, y=260)

Button(root, text="7", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=8, y=320)
Button(root, text="8", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=121, y=320)
Button(root, text="9", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=231, y=320)
Button(root, text="sin", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=341, y=320)
Button(root, text=">", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=451, y=320)
Button(root, text="-", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=561, y=320)

Button(root, text="4", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=8, y=380)
Button(root, text="5", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=121, y=380)
Button(root, text="6", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=231, y=380)
Button(root, text="cos", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=341, y=380)
Button(root, text="x", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=451, y=380)
Button(root, text="+", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=561, y=380)

Button(root, text="1", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=8, y=440)
Button(root, text="2", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=121, y=440)
Button(root, text="3", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=231, y=440)
Button(root, text="tan", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=341, y=440)
Button(root, text="y", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=451, y=440)

Button(root, text="π", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=8, y=500)
Button(root, text="0", width=9, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=121, y=500)
Button(root, text=".", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=341, y=500)
Button(root, text="e", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=451, y=500)
Button(root, text="=", width=4, height=3, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#F7A32A", command=lambda: clear()).place(x=561,  y=440)
Button(root, text="" , width=4, height=3, font=("arial", 30, "bold"), bg="#17161b", command=lambda: clear()).place(x=561, y=560)

#binding keys from keybord
root.bind('1', lambda event: clear())
root.bind('2', lambda event: clear())
root.bind('3', lambda event: clear())
root.bind('4', lambda event: clear())
root.bind('5', lambda event: clear())
root.bind('6', lambda event: clear())
root.bind('7', lambda event: clear())
root.bind('8', lambda event: clear())
root.bind('9', lambda event: clear())
root.bind('0', lambda event: clear())
root.bind('.', lambda event: clear())

root.bind('*', lambda event: clear())
root.bind('/', lambda event: clear())
root.bind('-', lambda event: clear())
root.bind('+', lambda event: clear())
root.bind('c', lambda event: clear())
root.bind('<Return>', lambda event: clear())
root.bind('<BackSpace>', lambda event: clear())



root.mainloop()