from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def labels(text, x, y):
    my_label = Label(text=text, font=("Arial", 16, "bold"))
    my_label.grid(column=x, row=y)

def button_clicked():
    result = round((float(entry.get()) * 1.609), 1)
    output.config(text=result)

labels("is equal to", 0, 1)
labels("Miles", 2, 0)
labels("Km", 2, 1)

output = Label(text=0, font=("Arial", 16, "bold"))
output.grid(column=1, row=1)

entry = Entry(width=10)
entry.focus()
entry.grid(column= 1, row= 0)

button = Button(text="Calculate", command=button_clicked)
button.grid(column= 1, row= 3)


window.mainloop()