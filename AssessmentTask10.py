import tkinter

window = tkinter.Tk()
window.geometry("400x200")
window.title('Nathaniel')
label = tkinter.Label(window, text='Ako si Nathaniel from BS ECE 2 - 2').pack(expand="YES")

def clickName():
    tkinter.Label(window, text="Pamantasan ng Lungsod ng Maynila", fg="red").pack()
tkinter.Button(window, text="Click me!", command=clickName, fg="blue").pack()
window.mainloop()