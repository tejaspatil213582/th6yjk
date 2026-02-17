import tkinter as tk
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x400")
root.resizable(False, False)

expression = ""
equation = tk.StringVar()

# Entry field
entry = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, relief=tk.SUNKEN, justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == 'C':
        action = clear
    else:
        action = lambda x=text: press(x)

    tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
              command=action).grid(row=row, column=col, sticky="nsew")

# Equal button
tk.Button(root, text='=', padx=20, pady=20, font=('Arial', 14),
          command=equalpress).grid(row=5, column=0, columnspan=4, sticky="nsew")

# Make buttons expandable
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
