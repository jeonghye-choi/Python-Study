from tkinter import *
def click():
    counter.set(counter.get() + 1)

if __name__=='__main__':
    window = Tk()
    window.title('Counter')
    counter = IntVar()
    counter.set(0)
    label = Label(window, textvariable=counter)
    label.pack()
    button = Button(window, text="Click Me", command=click)
    button.pack()
    window.mainloop()