import tkinter as tk

# 1. Seting up the main window
root = tk.Tk()
root.title("Basic Calculator")

# 2. Creating the display area
display = tk.Entry(root, width=35, borderwidth=5, font=("Arial", 12))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# 3. Defining the Functions to be used
def button_click(char):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(char))

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# 4. Create the Buttons (Numbers 0-9)
btn0 = tk.Button(root, text="0", padx=30, pady=20, command=lambda: button_click("0"))
btn1 = tk.Button(root, text="1", padx=30, pady=20, command=lambda: button_click("1"))
btn2 = tk.Button(root, text="2", padx=30, pady=20, command=lambda: button_click("2"))
btn3 = tk.Button(root, text="3", padx=30, pady=20, command=lambda: button_click("3"))
btn4 = tk.Button(root, text="4", padx=30, pady=20, command=lambda: button_click("4"))
btn5 = tk.Button(root, text="5", padx=30, pady=20, command=lambda: button_click("5"))
btn6 = tk.Button(root, text="6", padx=30, pady=20, command=lambda: button_click("6"))
btn7 = tk.Button(root, text="7", padx=30, pady=20, command=lambda: button_click("7"))
btn8 = tk.Button(root, text="8", padx=30, pady=20, command=lambda: button_click("8"))
btn9 = tk.Button(root, text="9", padx=30, pady=20, command=lambda: button_click("9"))

btn_div = tk.Button(root, text="/", padx=30, pady=20, command=lambda: button_click("/"))
btn_mult = tk.Button(root, text="*", padx=30, pady=20, command=lambda: button_click("*"))
btn_sub = tk.Button(root, text="-", padx=30, pady=20, command=lambda: button_click("-"))
btn_clear = tk.Button(root, text="C", padx=30, pady=20, command=clear_display)
btn_equal = tk.Button(root, text="=", padx=30, pady=20, command=calculate)
btn_add = tk.Button(root, text="+", padx=30, pady=20, command=lambda: button_click("+"))

# 5. Place the buttons on the Grid
# Row 1
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn_div.grid(row=1, column=3)

# Row 2
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn_mult.grid(row=2, column=3)

# Row 3
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn_sub.grid(row=3, column=3)

# Row 4
btn0.grid(row=4, column=0)
btn_clear.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)
btn_add.grid(row=4, column=3)

root.mainloop()
