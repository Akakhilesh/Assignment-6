from tkinter import *

# Creating Application Window
window = Tk()
window.title("Calculator")
window.geometry("230x280")

# creating display screen using Entry Widget
display=Entry(window,width=36,bd=5)
display.place(x=0,y=0)

# Creating click method for buttons(0-9)
def click(num):
    result=display.get()
    display.delete(0,END)
    display.insert(0,str(result) + str(num))

# Creating operation method for addtion, subtraction, multiplication and division
def add():
    n1=display.get()
    global math
    math="addition"
    global i
    i=int(n1)
    display.delete(0,END)

def sub():
    n1=display.get()
    global math
    math = "subtraction"
    global i
    i=int(n1)
    display.delete(0,END)

def multiply():
    n1=display.get()
    global math
    math = "multiplication"
    global i
    i=int(n1)
    display.delete(0,END)

def divide():
    n1=display.get()
    global math
    math = "division"
    global i
    i=int(n1)
    display.delete(0,END)

# using the 'global math' variable for conditional control statements
def equals():
    n2=display.get()
    display.delete(0,END)
    if math=="addition":
        display.insert(0,i+int(n2))
    elif math=="subtraction":
        display.insert(0,i-int(n2))
    elif math=="multiplication":
        display.insert(0,i*int(n2))
    elif math=="division":
        display.insert(0,i/int(n2))

# creating clear method to clear the display screen
def clear():
    display.delete(0,END)



# creation Buttons
num7=Button(window,text="7",width=6,height=3,bd=2,command=lambda:click(7))
num7.place(x=5,y=30)
num8=Button(window,text="8",width=6,height=3,bd=2,command=lambda:click(8))
num8.place(x=60,y=30)
num9=Button(window,text="9",width=6,height=3,bd=2,command=lambda:click(9))
num9.place(x=115,y=30)
div=Button(window,text="/",width=6,height=3,bd=2,command=divide)
div.place(x=170,y=30)
num4=Button(window,text="4",width=6,height=3,bd=2,command=lambda:click(4))
num4.place(x=5,y=90)
num5=Button(window,text="5",width=6,height=3,bd=2,command=lambda:click(5))
num5.place(x=60,y=90)
num6=Button(window,text="6",width=6,height=3,bd=2,command=lambda:click(6))
num6.place(x=115,y=90)
mul=Button(window,text="*",width=6,height=3,bd=2,command=multiply)
mul.place(x=170,y=90)
num1=Button(window,text="1",width=6,height=3,bd=2,command=lambda:click(1))
num1.place(x=5,y=150)
num2=Button(window,text="2",width=6,height=3,bd=2,command=lambda:click(2))
num2.place(x=60,y=150)
num3=Button(window,text="3",width=6,height=3,bd=2,command=lambda:click(3))
num3.place(x=115,y=150)
minus=Button(window,text="-",width=6,height=3,bd=2,command=sub)
minus.place(x=170,y=150)
clear=Button(window,text="C",width=6,height=3,bd=2, command=clear)
clear.place(x=5,y=210)
num0=Button(window,text="0",width=6,height=3,bd=2,command=lambda:click(0))
num0.place(x=60,y=210)
equal=Button(window,text="=",width=6,height=3,bd=2,command=equals)
equal.place(x=115,y=210)
plus=Button(window,text="+",width=6,height=3,bd=2,command=add)
plus.place(x=170,y=210)

# Mainloop
window.mainloop()