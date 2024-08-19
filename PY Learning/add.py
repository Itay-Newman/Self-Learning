import tkinter as tk
from tkinter import messagebox

BASES = {
    "Binary (2)": 2,
    "Octal (8)": 8,
    "Decimal (10)": 10,
    "Hexadecimal (16)": 16
}

OPERATIONS = ["Addition", "Subtraction", "Multiplication", "Division"]

def convert_to_base10(number, base):
    try:
        return int(number, base)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the given base.")
        return None

def convert_from_base10(number, base):
    try:
        number = int(number)
        if base == 10:
            return str(number)
        elif base == 2:
            return bin(number)[2:]
        elif base == 8:
            return oct(number)[2:]
        elif base == 16:
            return hex(number)[2:].upper()
        else:
            return "Unsupported base"
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid base.")
        return None

def perform_operation(num1, base1, num2, base2, result_base, operation):
    num1_base10 = convert_to_base10(num1, base1)
    num2_base10 = convert_to_base10(num2, base2)

    if num1_base10 is None or num2_base10 is None:
        return "Error in conversion"

    if operation == "Addition":
        result_base10 = num1_base10 + num2_base10
    elif operation == "Subtraction":
        result_base10 = num1_base10 - num2_base10
    elif operation == "Multiplication":
        result_base10 = num1_base10 * num2_base10
    elif operation == "Division":
        if num2_base10 == 0:
            return "Error: Division by zero"
        result_base10 = num1_base10 / num2_base10
    else:
        return "Unsupported operation"

    return convert_from_base10(result_base10, result_base)

def calculate_result():
    num1 = entry_number1.get()
    base1 = BASES[base_var1.get()]
    num2 = entry_number2.get()
    base2 = BASES[base_var2.get()]
    result_base = BASES[result_base_var.get()]
    operation = operation_var.get()

    result = perform_operation(num1, base1, num2, base2, result_base, operation)
    label_result.config(text=result)  # Directly set the result without the prefix

def copy_result():
    result_text = label_result.cget("text")
    root.clipboard_clear()
    root.clipboard_append(result_text)
    root.update()  # Now it stays on the clipboard

def main():
    global entry_number1, entry_number2, base_var1, base_var2, result_base_var, operation_var, label_result, root

    # GUI setup
    root = tk.Tk()
    root.title("Base Calculator")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    label_number1 = tk.Label(frame, text="Number 1:")
    label_number1.grid(row=0, column=0, sticky="e")
    entry_number1 = tk.Entry(frame)
    entry_number1.grid(row=0, column=1)

    label_base1 = tk.Label(frame, text="Base 1:")
    label_base1.grid(row=0, column=2, sticky="e")
    base_var1 = tk.StringVar(value="Decimal (10)")
    base_menu1 = tk.OptionMenu(frame, base_var1, *BASES.keys())
    base_menu1.grid(row=0, column=3)

    label_number2 = tk.Label(frame, text="Number 2:")
    label_number2.grid(row=1, column=0, sticky="e")
    entry_number2 = tk.Entry(frame)
    entry_number2.grid(row=1, column=1)

    label_base2 = tk.Label(frame, text="Base 2:")
    label_base2.grid(row=1, column=2, sticky="e")
    base_var2 = tk.StringVar(value="Decimal (10)")
    base_menu2 = tk.OptionMenu(frame, base_var2, *BASES.keys())
    base_menu2.grid(row=1, column=3)

    label_result_base = tk.Label(frame, text="Result Base:")
    label_result_base.grid(row=2, column=0, sticky="e")
    result_base_var = tk.StringVar(value="Decimal (10)")
    result_base_menu = tk.OptionMenu(frame, result_base_var, *BASES.keys())
    result_base_menu.grid(row=2, column=1)

    label_operation = tk.Label(frame, text="Operation:")
    label_operation.grid(row=2, column=2, sticky="e")
    operation_var = tk.StringVar(value="Addition")
    operation_menu = tk.OptionMenu(frame, operation_var, *OPERATIONS)
    operation_menu.grid(row=2, column=3)

    button_calculate = tk.Button(frame, text="Calculate", command=calculate_result)
    button_calculate.grid(row=3, column=0, columnspan=4, pady=10)

    button_copy = tk.Button(frame, text="Copy Result", command=copy_result)
    button_copy.grid(row=3, column=4, pady=10)

    label_result = tk.Label(frame, text="")
    label_result.grid(row=4, column=0, columnspan=5)

    root.mainloop()

if __name__ == "__main__":
    main()
