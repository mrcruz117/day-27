import tkinter

window = tkinter.Tk()
window.title("My first Python GUI")
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="This is a Label", font=("Roboto",24,"bold"))
my_label.pack(side="left")

window.mainloop()
