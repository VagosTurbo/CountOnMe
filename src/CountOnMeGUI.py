import tkinter
from tkinter import *



#generating and configuring window
root = Tk()
root.title("CountOnMe")
p1 = PhotoImage(file = 'CountOnMelogo_FINAL.png')
root.iconphoto(False, p1)
root.geometry("570x470+100+100")
root.resizable(False, False)
root.configure(bg="#17161b")

#variable for equation
equation = ""

#displaying numbers on display
def show(value):
    global equation
    equation += value
    display.config(text = equation)
    

def remove():
    global equation
    equation = equation[:-1]
    display.config(text = equation)

def negation():
    global equation
    buffer = float(equation)
    buffer = -1*buffer
    equation = str(buffer)
    display.config(text = equation)

#clears the display and equation
def clear():
    global equation
    equation = ""
    display.config(text = equation)

#after hitting '=' starts calculating and showing result on display
def calculate():
    global equation
    result = ""
    if equation !="":
        try:
            result = eval(equation)
            equation = str(result)
        except:
            result = "error"
            equation = ""
    display.config(text=result)


#generating a window for equation/result
display = Label(root, width = 25, height = 2, text = "", font = ("arial", 30))
display.pack()

#making and configuring buttons
Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#289cbf", command=lambda: clear()).place(x=8, y=100)
Button(root, text="<=", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#31BED7", command=lambda: remove()).place(x=141, y=100)
Button(root, text="x!", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("!")).place(x=281, y=100)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("/")).place(x=421, y=100)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*")).place(x=421, y=160)

Button(root, text="^x", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("^")).place(x=8, y=160)
Button(root, text="√", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("√")).place(x=141, y=160)
Button(root, text="+/-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: negation()).place(x=281, y=160)
#Button(root, text=")", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(")")).place(x=421, y=160)

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
Button(root, text="=", width=5, height=2, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#F7A32A", command=lambda: calculate()).place(x=421, y=340)

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
root.bind('<Return>', lambda event: calculate())
root.bind('<BackSpace>', lambda event: remove())



root.mainloop()