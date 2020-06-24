from tkinter import *

class Calc(Frame):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.entry = Entry(self, width=12, justify=RIGHT)
        self.entry.insert(0, '0')
        self.entry.pack()
        for label in '10CD':
            btn = Button(self, text=label, width=3, command=(lambda c=label: self.enter(c)))
            btn.pack(side=LEFT)

if __name__ == '__main__':
    window = Tk()
    window.title('Calc')
    calc = Calc(window)
    calc.pack()
    window.mainloop()