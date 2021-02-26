from tkinter import *


def miles_to_kms():
    km = round(float(miles_input.get()) * 1.609,3)
    result_label.config(text=km)

window = Tk()
window.title("Miles to Kms")
window.config(padx=40, pady=40)

miles_input = Entry(width=15)
miles_input.grid(column=1, row=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)
result_label = Label(text="0")
result_label.grid(column=1, row=1)
kms_label = Label(text="Kms")
kms_label.grid(column=2, row=1)
calculate_button = Button(text="Calculate", command=miles_to_kms)
calculate_button.grid(column=1, row=2)

window.mainloop()