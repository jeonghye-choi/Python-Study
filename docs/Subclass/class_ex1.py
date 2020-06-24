from tkinter import *

class Calc:
    def enter(self, label):
        if label == 'C':
            self.entry.delete(0, END)
            self.entry.insert(0, '0')
        elif label == 'D':
            ans = eval(self.entry.get())
            ans *= 2
            self.entry.delete(0, END)
            self.entry.insert(0, ans)
        elif self.entry.get() == '0':
            self.entry.delete(0, END)
            self.entry.insert(END, label)
        else:
            self.entry.insert(END, label)
    
    def __init__(self):
        self.win = Tk()
        self.win.title('Calc')
        self.entry = Entry(self.win, width=12, justify=RIGHT)
        self.entry.insert(0, '0')
        self.entry.pack()
        frm = Frame(self.win)
        frm.pack()
        for label in '10CD':
            btn = Button(frm, text=label, width=3, command=(lambda c=label: self.enter(c)))
            btn.pack(side=LEFT)
        self.win.mainloop()

if __name__=='__main__':
    c = Calc()

