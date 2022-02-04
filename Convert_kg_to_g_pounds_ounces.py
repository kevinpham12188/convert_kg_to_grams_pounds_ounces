from tkinter import *

window = Tk()


def convert():
    g = int(kg_input.get()) * 1000
    p = int(kg_input.get()) * 2.20462
    o = int(kg_input.get()) * 35.274

    grams.insert(END, g)
    pounds.insert(END, p)
    ounces.insert(END, o)


kg_label = Label(window, text="Kg")
kg_label.grid(row=0, column=0)

input_1 = StringVar()
kg_input = Entry(window, textvariable=input_1)
kg_input.grid(row=0, column=1)

convert_button = Button(window, text="Convert", command=convert)
convert_button.grid(row=0, column=2)

grams = Text(window, height=1, width=20)
grams.grid(row=1, column=0)

pounds = Text(window, height=1, width=20)
pounds.grid(row=1, column=1)

ounces = Text(window, height=1, width=20)
ounces.grid(row=1, column=2)


window.mainloop()