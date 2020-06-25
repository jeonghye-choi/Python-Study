from tkinter import *

window = Tk()
window.title("Python")
frm1 = Frame(window)
frm1.pack()
frm2 = Frame(window, borderwidth=4, relief=GROOVE)
frm2.pack(side=LEFT)
frm3 = Frame(window, borderwidth=4, relief=GROOVE)
frm3.pack(side=RIGHT)

lbl1 = Label(frm1, text="First label")
lbl1.pack()
lbl2 = Label(frm2, text="Second label")
lbl2.pack()
lbl3 = Label(frm2, text="Third label")
lbl3.pack()
lbl4 = Label(frm3, text="Fourth label")
lbl4.pack()
window.mainloop()