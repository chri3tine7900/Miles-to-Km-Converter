from tkinter import *

def miles_to_km():
    try:
        miles = float(input.get())
        km = miles * 1.609
        kilometer_result_label.config(text=f"{km:.2f}")  # Format to 2 decimal places
    except ValueError:
        kilometer_result_label.config(text="Invalid input. Please enter a number.")

def km_to_miles():
    try:
        km = float(input.get())
        miles = km / 1.609
        kilometer_result_label.config(text=f"{miles:.2f}")
    except ValueError:
        kilometer_result_label.config(text="Invalid input. Please enter a number.")

def clear_fields():
    input.delete(0, 'end')  # Clear the input field
    kilometer_result_label.config(text="0")

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=150, pady=150)

my_Label = Label(window, text="Input", font=("Arial", 15, "bold"))
my_Label.grid(column=4, row=4)

my_Label2 = Label(window, text="Distance", font=("Arial", 15, "bold"))
my_Label2.grid(column=4, row=5)

my_Label3 = Label(window, text="is equal to", font=("Arial", 15, "bold"))
my_Label3.grid(column=1, row=5)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=3, row=5)

input = Entry(width=30)
input.grid(column=3, row=4)

miles_button = Button(text="Miles to Km", width=10, command=miles_to_km)
miles_button.grid(column=3, row=6)

km_button = Button(text="Km to Miles", width=10, command=km_to_miles)
km_button.grid(column=3, row=7)

clear_button = Button(text="Clear", width=10, command=clear_fields)
clear_button.grid(column=3, row=8)

window.mainloop()
