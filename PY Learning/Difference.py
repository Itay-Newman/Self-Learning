import datetime
import tkinter as tk
from tkinter import messagebox


def calculate_difference():
    try:
        date_str = entry_date.get()
        date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
        today = datetime.datetime.now()
        difference = today - date

        unit = unit_var.get()
        if unit == "Days":
            result = difference.days
        elif unit == "Weeks":
            result = difference.days / 7
        elif unit == "Months":
            result = difference.days / 30.44  # average days per month
        elif unit == "Hours":
            result = difference.total_seconds() / 3600
        elif unit == "Minutes":
            result = difference.total_seconds() / 60
        elif unit == "Seconds":
            result = difference.total_seconds()
        else:
            result = difference.days  # default to days if something goes wrong

        result_label.config(text=f"The difference is {result:.2f} {unit.lower()}.")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter the date in the format: dd/mm/yyyy")


# Set up the main application window
root = tk.Tk()
root.title("Date Difference Calculator")

# Set up the input field and label
tk.Label(root, text="Enter the date in the format: dd/mm/yyyy").pack(pady=10)
entry_date = tk.Entry(root)
entry_date.pack(pady=5)

# Set up the dropdown menu for unit selection
unit_var = tk.StringVar(root)
unit_var.set("Days")  # default value
unit_menu = tk.OptionMenu(root, unit_var, "Months", "Weeks", "Days", "Hours", "Minutes", "Seconds")
unit_menu.pack(pady=10)

# Set up the button to calculate the difference
tk.Button(root, text="Calculate Difference", command=calculate_difference).pack(pady=10)

# Set up the label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()
