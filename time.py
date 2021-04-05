from time import strftime
from tkinter import Label, Tk

window = Tk()
window.title("Clock")
window.geometry("400x100")
window.configure(bg="black")
window.resizable(False, False)

clock_label = Label(window, bg="black", fg="cyan", font=("ds-digital", 30), relief='flat')
clock_label.place(x=20, y=20)


def update_label():
    current_time = strftime('%d/%m/%y               %H: %M: %S')
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label)


update_label()
window.mainloop()
