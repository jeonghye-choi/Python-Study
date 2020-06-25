from tkinter import *

def click(incr):
    global count
    count.set(count.get() + incr)

def main():
    global count
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

if __name__=='__main__':
    main()
    