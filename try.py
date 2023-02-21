from tkinter import *

window = Tk()
window.geometry("200x100")
attribute = IntVar()


def get_attribute():
    selection = "the selected symbol is a " + str(attribute.get())
    test_out.config(text=selection)


def submit_variable():
    global attribute
    attribute.set("0")

submit_button = Button(window, text="Submit", width=10, height=2, command=submit_variable)
submit_button.pack()

var = Radiobutton(window, text="variable", variable=attribute, value=1, command=get_attribute)
var.pack()

test_out = Label(window, text="the selected symbol is a ")
test_out.pack()

window.mainloop()