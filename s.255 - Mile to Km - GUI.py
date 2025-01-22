from tkinter import *

def miles_to_km():
    try:
        miles = float(input.get())
        km = miles * 1.609
        kilometer_result_label.config(text=f"{km}")
    except ValueError:
        kilometer_result_label.config(text="Input must be a number")

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=150, pady=150)

my_Label = Label(window, text="Miles", font=("Arial", 15, "bold"))
my_Label.grid(column=4, row=4)

my_Label2 = Label(window, text="Km", font=("Arial", 15, "bold"))
my_Label2.grid(column=4, row=5)

my_Label3 = Label(window, text="is equal to", font=("Arial", 15, "bold"))
my_Label3.grid(column=1, row=5)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=3, row=5)

input = Entry(width=30)  # Increased width to 15 
print(input.get())
input.grid(column=3, row=4)

button = Button(text="Calculate", width=10, command=miles_to_km)
button.grid(column=3, row=6)

window.mainloop()