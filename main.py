from tkinter import *

window = Tk()
window.title("My first Python GUI")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="This is a Label", font=("Roboto", 24, "bold"))
my_label.pack()
my_label.config(text="New Text")


# button
def button_click():
    print("Clicked!")
    my_label.config(text=f"{input.get()}")
    input.delete(0, len(input.get()))


button = Button(text="click me", command=button_click)
button.pack()

# Entry
input = Entry(width=10)
input.pack()
print(input.get())

window.mainloop()
