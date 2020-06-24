# Encapsulating Using Subclasses

## 📙 contents

1. Referencing Environment

2. A Slight Problem and Solution

    - Big Function

    - Class

    - Subclass

3. A Short Comparison of Encapsulating Method

### 📖 Referencing Environment

- dir()

    : 해당 객체(인자)가 어떤 변수와 메소드를 가지고 있는지 나열

- locals()

    : 현재의 local 변수를 dict type으로 return

- globals()

    : 현재의 global 변수를 dict type으로 return

- 🔎 Namespace 네임스페이스

    특정한 객체(object)를 이름(name)에 따라 구분할 수 있는 범위

    프로그래밍을 수행하다보면 모든 변수 이름과 함수 이름을 정하는 것이 중요한데 이들 모두를 겹치지 않게
    정하는 것은 사실상 불가능하다

    따라서 네임스페이스를 이용해, 특정한 하나의 이름이 통용될 수 있는 범위를 제한한다.

    즉, 소속된 네임스페이스가 다르다면 같은 이름이 다른 개체를 가리키도록 하는 것이 가능해진다

    <a href="https://hcnoh.github.io/2019-01-30-python-namespace">참고</a>


### 📖 2-1 Function

- function ex1

    ```py
    from tkinter import *

    def enter(label):
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

    if __name__ == '__main__':
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
    ```

- ex1 -> main함수

    ```py
    # function_ex1 을 main함수로 정의 
    # --> error : 변수가 main함수 안에 있기때문에!(local)
    # => global

    from tkinter import *

    def enter(label):
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

    ```
    이 경우에는 Error발생

    변수가 범위를 벗어나서 사용되었다 => global

- global로 바꾸기

    ```py
    from tkinter import *

    entry = None
    def enter(label):
        global entry
        ...

    def main():
        global entry
        ...

    if __name__ == '__main__':
        main()

    ```

- 🔎 global vs nonlocal

    global: 전역변수 바꿈

    nonlocal: 한단계 위만 바꿈

    - <a href="https://devbruce.github.io/python/py-13-global,nonlocal/">참고</a>

    - SyntaxError: no binding for nonlocal 'entry' found

        : global과 nonlocal의 차이점 -> nonlocal은 함수 내부에서 변수값을 정의를 해줘야함!!

        <a href="https://www.python-course.eu/python3_global_vs_local_variables.php">참고</a>


### 📖 2-2 Class

- Making a Class for Calc

    **- self사용**
    ```py
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
    ```

### 📖 2-3 Subclass

- Making Calc as a Subclass

    ```py
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
    ```

    - **super**

    - *args, **kwargs

        파이썬에서는 두종류의 인자가 있다. positional과 keyword

        positional은 튜플로, keyword는 딕셔너리로 다룬다 

        <a href="https://brunch.co.kr/@princox/180">참고</a>


### 📖 2 장단점

![image](https://user-images.githubusercontent.com/54584063/85611079-8faa3b00-b692-11ea-8028-43ac798d75be.png)


### 📖 arguments

- list arguments

    ```py
    prod = lambda *ls: functools.reduce(lambda x, y: x*y, ls, 1)
    ```
- keyword arguments
    unwrap a list -> prefix * for this case

    ```py
    ns = list(range(1, 5))
    print(prod(*ns))  # prod(1, 2, 3, 4)와 같은 말!
    ```
