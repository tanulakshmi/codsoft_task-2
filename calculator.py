from tkinter import *
from tkinter import font

# Functions for window controls
def minimize_window():
    window.state('iconic')

def maximize_window():
    if window.state() == 'normal':
        window.state('zoomed')
    else:
        window.state('normal')

def close_window():
    window.destroy()

def drag_window(event):
    x = window.winfo_pointerx() - event.widget.winfo_rootx()
    y = window.winfo_pointery() - event.widget.winfo_rooty()
    window.geometry(f"+{x}+{y}")

# Functionality for Calculator
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    result = str(eval(expression))  # 'eval' is used for evaluating the string expressions directly
    input_text.set(result)
    expression = result

window = Tk()
window.geometry("400x500")
window.config(bg="#343a40")
window.overrideredirect(True)  # This removes the window's title bar, border, and controls

custom_font = font.Font(family="Helvetica", size=12, weight="bold")
title_bar = Frame(window, bg='#495057', relief='raised', bd=0)
title_bar.pack(fill=X)

title_text = Label(title_bar, text="Calculator", bg='#495057', fg='white', font=custom_font)
title_text.pack(side=LEFT, padx=10)

close_button = Button(title_bar, text='X', command=close_window, bg='red', fg='white', padx=10, pady=2, borderwidth=0)
close_button.pack(side=RIGHT)

minimize_button = Button(title_bar, text='-', command=minimize_window, bg='gray', fg='white', padx=10, pady=2, borderwidth=0)
minimize_button.pack(side=RIGHT)

maximize_button = Button(title_bar, text='□', command=maximize_window, bg='gray', fg='white', padx=10, pady=2, borderwidth=0)
maximize_button.pack(side=RIGHT)

title_bar.bind("<ButtonPress-1>", drag_window)
title_bar.bind("<B1-Motion>", drag_window)

expression = ""
input_text = StringVar()

# Input/Output Screen
input_frame = Frame(window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=55, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Buttons Frame
btns_frame = Frame(window, bg='black')
btns_frame.pack()

# First row
clear = Button(btns_frame, text="C", fg="black", width=32, height=2, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_clear())
clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("/"))
divide.grid(row=0, column=3, padx=1, pady=1)

# Second row
seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click(7))
seven.grid(row=1, column=0, padx=1, pady=1)

eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click(8))
eight.grid(row=1, column=1, padx=1, pady=1)

nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click(9))
nine.grid(row=1, column=2, padx=1, pady=1)

multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("*"))
multiply.grid(row=1, column=3, padx=1, pady=1)

# Third row
four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click(4))
four.grid(row=2, column=0, padx=1, pady=1)

five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click(5))
five.grid(row=2, column=1, padx=1, pady=1)

six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click(6))
six.grid(row=2, column=2, padx=1, pady=1)

minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("-"))
minus.grid(row=2, column=3, padx=1, pady=1)

# Fourth row
one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click(1))
one.grid(row=3, column=0, padx=1, pady=1)

two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click(2))
two.grid(row=3, column=1, padx=1, pady=1)

three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click(3))
three.grid(row=3, column=2, padx=1, pady=1)

plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("+"))
plus.grid(row=3, column=3, padx=1, pady=1)

# Fifth row
zero = Button(btns_frame, text="0", fg="Black", width=23, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click(0))
zero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

dot = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click('.'))
dot.grid(row=4, column=2, padx=1, pady=1)

equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=btn_equal)
equals.grid(row=4, column=3, padx=1, pady=1)

window.mainloop()
