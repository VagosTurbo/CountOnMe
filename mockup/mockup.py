import tkinter
from tkinter import *
from tkinter import messagebox
import re

#generating and configuring window
root = Tk()
root.title("CountOnMe")
#p1 = PhotoImage(file = 'CountOnMelogo_FINAL.png')
#root.iconphoto(False, p1)
root.geometry("570x470+100+100")
root.resizable(False, False)
root.configure(bg="#17161b")



#clears the display and equation
def clear():
    global equation
    equation = ""
    display.config(text = equation)


#generating a window for equation/result
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
menubar.add_command(label="Help", command=lambda: messagebox.showinfo("Help", "".join(help_message)))

modes = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Modes", menu = modes)
modes.add_command(label="Standard - basic calculator", command=lambda: messagebox.showinfo("Modes", "There are 3 modes in this calculator:\n\n1. Standard - basic calculator\n2. Scientific - advanced calculator\n3. Programmer - binary calculator"))
modes.add_command(label="Scientific - advanced calculator")
modes.add_command(label="Programmer - binary calculator")

# display the menubar
root.config(menu=menubar)

#making and configuring buttons
Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#289cbf", command=lambda: clear()).place(x=8, y=100)
Button(root, text="⌫", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#31BED7", command=lambda: clear()).place(x=141, y=100)
Button(root, text="x!", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=281, y=100)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=421, y=160)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=421, y=100)

Button(root, text="xʸ", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=8, y=160)
Button(root, text="ˣ√y", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=141, y=160)
Button(root, text="+/-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=281, y=160)

Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=8, y=220)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=141, y=220)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=281, y=220)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=421, y=220)

Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=8, y=280)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=141, y=280)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=281, y=280)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=421, y=280)

Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=8, y=340)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=141, y=340)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=281, y=340)
Button(root, text="0", width=12, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=8, y=400)

Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=281, y=400)
Button(root, text="=", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#F7A32A", command=lambda: clear()).place(x=421,  y=340)
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