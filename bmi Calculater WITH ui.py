import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height * height)
    messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create labels and entries for weight and height
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0)

weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

height_label = tk.Label(root, text="Height (m):")
height_label.grid(row=1, column=0)

height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2)

# Run the application
root.mainloop()