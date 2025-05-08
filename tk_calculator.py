import tkinter as tk
from tkinter import messagebox
import math  # Required for square root


def calculate(operation):
    try:
        num1 = float(entry1.get())

        # For binary operations
        if operation in ["add", "subtract", "multiply", "divide"]:
            num2 = float(entry2.get())

        if operation == "add":
            result.set(num1 + num2)
        elif operation == "subtract":
            result.set(num1 - num2)
        elif operation == "multiply":
            result.set(num1 * num2)
        elif operation == "divide":
            if num2 != 0:
                result.set(num1 / num2)
            else:
                messagebox.showerror("Error", "Cannot divide by zero.")
        elif operation == "square":
            result.set(num1 ** 2)
        elif operation == "sqrt":
            if num1 >= 0:
                result.set(math.sqrt(num1))
            else:
                messagebox.showerror("Error", "Cannot take square root of a negative number.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


root = tk.Tk()
root.title("Extended Calculator")


tk.Label(root, text="Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)


result = tk.StringVar()
tk.Label(root, text="Result:").grid(row=2, column=0)
tk.Entry(root, textvariable=result, state='readonly').grid(row=2, column=1)


# Binary operation buttons
tk.Button(root, text="Add", command=lambda: calculate("add")).grid(row=3, column=0)
tk.Button(root, text="Subtract", command=lambda: calculate("subtract")).grid(row=3, column=1)
tk.Button(root, text="Multiply", command=lambda: calculate("multiply")).grid(row=4, column=0)
tk.Button(root, text="Divide", command=lambda: calculate("divide")).grid(row=4, column=1)

# Unary operation buttons
tk.Button(root, text="Square", command=lambda: calculate("square")).grid(row=5, column=0)
tk.Button(root, text="Square Root", command=lambda: calculate("sqrt")).grid(row=5, column=1)


root.mainloop()
