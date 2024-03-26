#steps:
#step1:Import Tkinter
#step2:GUI Interaction
#step3:Adding Inputs
#step4:main loop



import tkinter as tk   #imported tkinter


# Function to perform arithmetic operations
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result = "Error! Division by zero"
            else:
                result = num1 / num2

        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, result)
    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, "Invalid input")


# GUI interaction
app = tk.Tk()
app.title("Simple Calculator")

# adding input fields
entry_num1 = tk.Entry(app, width=10)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

operation_var = tk.StringVar(app)
operations = ['+', '-', '*', '/']
operation_var.set('+')  # Default operation is addition
dropdown_operation = tk.OptionMenu(app, operation_var, *operations)
dropdown_operation.grid(row=0, column=1, padx=5, pady=5)

entry_num2 = tk.Entry(app, width=10)
entry_num2.grid(row=0, column=2, padx=5, pady=5)

# Create Calculate button
button_calculate = tk.Button(app, text="Calculate", command=calculate)
button_calculate.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="WE")

# Create result field
entry_result = tk.Entry(app, width=30)
entry_result.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# mainloop
app.mainloop()
