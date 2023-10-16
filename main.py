from tkinter import *

FONT = ("Arial", 20)


def button_clicked():
    miles = float(miles_input.get())
    miles_to_km = round(miles * 1.6, 1)
    calculation_label.config(text=f"{miles_to_km}")


window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)


# Labels
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font=FONT)
is_equal_to_label.grid(column=0, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

calculation_label = Label(text=0, font=FONT)
calculation_label.grid(column=1, row=1)

# Button
calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

# Entry
miles_input = Entry(width=10)
print(miles_input.get())
miles_input.grid(column=1, row=0)

window.mainloop()
