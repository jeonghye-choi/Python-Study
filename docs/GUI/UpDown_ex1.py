from tkinter import *

def click(incr):
    count.set(count.get() + incr)

if __name__=='__main__':
    window = Tk()
    window.title("up&down")

    count = IntVar()
    count.set(0)
    label = Label(window, textvariable=count)
    label.pack()

    button = Button(window, text="UP", command=lambda : click(1))
    button.pack()

    button = Button(window, text="DOWN", command= lambda : click(-1))
    button.pack()

    window.mainloop()