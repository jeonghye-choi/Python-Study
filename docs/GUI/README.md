# GUI

Graphical User Interface

## 📙 contents

1. CUI and GUI
2. Making GUI Programs using Tkinter
3. Mutable Types
4. Event Handling
5. Lambda function

6. Default Arguments
7. Layout Management
8. Changing Style
9. Function eval
10. Example: Calculator


### 📖 GUI

two kinds of Interface

- CUI: command-line user Interface

- GUI: graphical user interface


### 📖 Tkinter

1. Making a **Root Window**

    ```py
    from tkinter import *

    window = Tk()
    window.title('Tkinter')
    window.mainloop()
    ```

2. Adding **Label**

    ```py
    from tkinter import *

    window = Tk()
    window.title('Tkinter')

    label = Label(window, text="This is our label.")
    label.pack()

    window.mainloop()
    ```

### 📖 Tkinter Mutable Types(변하기 쉬운)

    |  <center>Python Immutable Type</center> |  <center>Tkinter Mutable Type</center> |
    |:--------|:--------:|--------:|
    |<center>int</center> | <center>IntVar</center> |
    |<center>string</center> | <center>StringVar</center> |
    |<center>bool</center> | <center>BooleanVar</center> |
    |<center>double</center> | <center>DoubleVar</center> |

    - 텍스트 Label은 바꿀 수 없다 -> text is fixed


### 📖 Event Handling

you can handle it by specifying a handler for a widget
```py
button = Button(window, text="Click Me", command=H)
```

- Example: Handling Button Click

    ```py
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
    ```

- Example: Up&Down

    ```py
    # UpDown_ex1
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
    ```

### 📖 Default Arguments

```py
def incr(count, gamma=1, delta=2):
    print(f"{count}. gamma: {gamma}, delta: {delta}")

if __name__ == '__main__':
    incr(1)  #1. gamma: 1, delta: 2
    incr(2,2)  #2. gamma: 2, delta: 2
    incr(3,2,1)  #3. gamma: 2, delta: 1
    incr(4, delta=5)  #4. gamma: 1, delta: 5
```

### 📖 Frame

A frame can be visible by showing the border

- Grouping labels with a frame

    ```py
    from tkinter import *

    window = Tk()
    window.title("Python")
    frm1 = Frame(window)
    frm1.pack()
    frm2 = Frame(window)
    frm2.pack()
    lbl1 = Label(frm1, text="First label")
    lbl1.pack()
    lbl2 = Label(frm2, text="Second label")
    lbl2.pack()
    lbl3 = Label(frm2, text="Third label")
    lbl3.pack()
    window.mainloop()
    ```
- relief 설정 속성

    ![image](https://user-images.githubusercontent.com/54584063/85804513-cb253200-b784-11ea-88ec-0c32fa888aed.png)



### 📖 Layout Using **Pack, Grid, Absolute Position(place)**
- #### pack

    ```py
    #layoutPack_ex1.py
    ...
    frm2 = Frame(window, borderwidth=4, relief=GROOVE)
    frm2.pack(side=LEFT)
    frm3 = Frame(window, borderwidth=4, relief=GROOVE)
    frm3.pack(side=RIGHT)
    ...
    ```
- #### Grid

    ```py
    ...
    btn1 = Button(frm1, text='First btn')
    btn1.grid(row=0, column=0)
    btn2 = Button(frm1, text='Second btn')
    btn2.grid(row=1, column=1)
    btn3 = Button(frm1, text='Third btn')
    btn3.grid(row=0, column=1)
    ...
    ```
- #### place: Absolute Position

    ```py
    from tkinter import *

    window = Tk()
    window.title('Python')
    window.geometry("250x200+30+30")

    btn1 = Button(window, text='First btn')
    btn1.place(x=20, y=20)
    btn2 = Button(window, text='Second btn')
    btn2.place(x=50, y=100)
    btn3 = Button(window, text='Third btn')
    btn3.place(x=110, y=40)
    ```

### 📖 Changing Style

- #### Font
    ```py
    button = Button(window, text="Hello", font=('Courier', 14, 'bold'))
    ```

- #### Color

    ```py
    button = Button(window, text="Hello", bg='green', fg='blue')

    ```


### 📖 Function **eval()**

It evaluates an expression written as a string

```py
eval("2+3*4")   #14
eval("0o10")   #8
eval("list('abc')")   #['a', 'b', 'c']
```

### 📖 Example: Calculator

```py
from tkinter import *

def enter(label):
    if label == 'C':
        entry.delete(0, END)
        entry.insert(0, '0')
    elif label == 'D':
        ans = eval(entry.get())
        ans *= 2
    elif entry.get() == '0':
        entry.delete(0, END)
        entry.insert(END, label)
    else:
        entry.insert(END, label)

if __name__ == '__main__':
    window = Tk()
    window.title('Calc')
    entry = Entry(window, width=12, justify=RIGHT)
    entry.insert(0, '0')
    entry.pack()
    frm = Frame(window)
    frm.pack()
    for label in '10CD':
        btn = Button(frm, text=label, width=3, command=(lambda char=label: enter(char)))
        btn.pack(side=LEFT)

    window.mainloop()
```

