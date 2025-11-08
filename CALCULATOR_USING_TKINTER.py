from tkinter import *
import math
window = Tk()
window.geometry("350x550")
window.config(bg="darkgrey")
window.title("Calculator")
e = Entry(window, width=20, borderwidth=5, font=("Arial", 20), bg="white", fg="black")
e.place(x=20, y=20)
def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))
def clear():
    e.delete(0, END)
def equal():
    try:
        expression = e.get()
        # Replace math functions with math module equivalents
        expression = expression.replace("sin", "math.sin")
        expression = expression.replace("cos", "math.cos")
        expression = expression.replace("tan", "math.tan")
        expression = expression.replace("sqrt", "math.sqrt")
        result = eval(expression)
        e.delete(0, END)
        e.insert(0, str(result))
    except Exception as ex:
        e.delete(0, END)
        e.insert(0, "Error")
buttons = [
    ("sin", lambda: click("sin("), 0, 200), ("cos", lambda: click("cos("), 85, 200),
    ("tan", lambda: click("tan("), 170, 200), ("sqrt", lambda: click("sqrt("), 260, 200),
    ("AC", clear, 0, 260), ("(", lambda: click("("), 85, 260),
    (")", lambda: click(")"), 170, 260), ("/", lambda: click("/"), 260, 260),
    ("7", lambda: click("7"), 0, 320), ("8", lambda: click("8"), 85, 320),
    ("9", lambda: click("9"), 170, 320), ("*", lambda: click("*"), 260, 320),
    ("4", lambda: click("4"), 0, 380), ("5", lambda: click("5"), 85, 380),
    ("6", lambda: click("6"), 170, 380), ("-", lambda: click("-"), 260, 380),
    ("1", lambda: click("1"), 0, 440), ("2", lambda: click("2"), 85, 440),
    ("3", lambda: click("3"), 170, 440), ("+", lambda: click("+"), 260, 440),
    ("Exit", window.quit, 0, 500), ("0", lambda: click("0"), 85, 500),
    (".", lambda: click("."), 170, 500), ("=", equal, 260, 500)
]
for (text, cmd, x, y) in buttons:
    Button(window, text=text, width=10, height=2, command=cmd,
           bg="black" if text not in "0123456789." else "grey", fg="white").place(x=x, y=y)
window.mainloop()