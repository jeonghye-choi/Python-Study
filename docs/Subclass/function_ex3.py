from tkinter import *

entry = None
def enter(label):
    global entry
    if label == 'C':
        entry.delete(0, END)
        entry.insert(0, '0')
    elif label == 'D':
        ans = eval(entry.get())
        ans *= 2
        entry.delete(0, END)
        entry.insert(0, ans)
    elif entry.get() == '0':
        entry.delete(0, END)
        entry.insert(END, label)
    else:
        entry.insert(END, label)

def main():
    global entry
    window = Tk()
    window.title('Calc')
    entry = Entry(window, width=12, justify=RIGHT)
    entry.insert(0, '0')
    entry.pack()
    frm = Frame(window)
    frm.pack()
    for label in '10CD':
        btn = Button(frm, text=label, width=3, command=(lambda c=label: enter(c)))
        btn.pack(side=LEFT)
    window.mainloop()

if __name__ == '__main__':
    main()
