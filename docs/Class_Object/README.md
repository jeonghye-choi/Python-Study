# Class and OOP

## 📙 contents

1. OOPS
2. Class and Object
3. Matrix Class
4. know Your **self**
5. Special Methods: __init__, __str__, __getitem__, __setitem__


### 📖 OOPS

Object-Oriented Programming (객체지향)

OOP를 사용하여 반복되는 코드를 없애고 사전이나 리스트가 지원하지 않는 상속과 같은
클래스의 기능을 사용할 수 있다

- Example: Printing Matrix

    ```py
    ns = list(range(1,7))
    m = [ns[n:n+3] for n in range(0,6,3)]

    def printMatrix(m):
        for row in m:
            rows = [str(e) for e in row]
            print(" ".join(rows))
    ```

### 📖 Class

- Class variable (클래스 변수)

    클래스이름.변수이름

    "self.변수이름"도 가능!

    파이썬은 이름을 찾을 때 

    1.인스턴스 네임스페이스 -> 2.클래스 네임스페이스 -> 3.수퍼 네임스페이스

    반대로는 찾지 않음! 즉, 자식이 부모의 네임스페이스를 참조할 수 있는데, 부모가 자식의 네임스페이스를
    참조할 수는 없다.

    ```py
    #ex: 모든 직원 연봉 인상
    class Employee(object):
        raise_amount = 1.1

        def __init__(self, first, lass, pay):
            self.first = first
            self.last = last
            self.pay = pay
            self.email = first.lower() + '.' + last.lower() + '@naver.com'
        
        def full_name(self):
            return f"{self.first} {self.last}"

        def apply_raise(self):
            self.pay = int(self.pay * Employee.raise_amount) ## self도 가능!클래스 이름 써줘야함!
    emp_1 = Employee("Jeonghye", "Choi", 100000)
    emp_2 = Employee("Sugin", "Kim", 50000)

    print(emp_1.pay)  #기존연봉
    emp_1.apply_raise()  #인상률 적용
    print(emp_1.pay)  #오른연봉
    ```
    self.raise_amount를 사용하면 파이썬은 처음엔 "인스턴스 네임스페이스"에서 "raise_amount"라는 이름을 찾고
    없으면 클래스 네임스페이스에서 찾는다

- 클래스변수 + 인스턴스변수

    모든 직원에 적용(클래스 변수) + 특별한 사람에게 인상률 적용(인스턴스 변수)

    ```py
    #ex: 특별 대상자 인상률 적용
    class Employee(object):
        raise_amount = 1.1
        ...

    emp_1 = Employee("Jeonghye", "Choi", 100000)
    emp_2 = Employee("Sugin", "Kim", 50000)

    emp_1.raise_amount = 1.2  #인스턴스 변수를 사용해 특별 인상률 적용
    ```

    ```py
    #ex: 직원 수 관리
    class Employee(object):
    
        raise_amount = 1.1
        num_of_emps = 0  #1 클래스 변수 정의
        
        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
            self.email = first.lower() + '.' + last.lower() + '@schoolofweb.net'
            
            Employee.num_of_emps += 1  #2 인스턴스가 생성될 때마다 1씩 증가

        def __del__(self):
            Employee.num_of_emps -= 1  #3 인스턴스가 제거될 때마다 1씩 감소
            
        def full_name(self):
            return '{} {}'.format(self.first, self.last)
        
        def apply_raise(self):
            self.pay = int(self.pay * self.raise_amount)  #1 인스턴스 변수부터 참조를 합니다.

    print Employee.num_of_emps  # 처음 직원 수
    emp_1 = Employee('Sanghee', 'Lee', 50000)  # 직원 1명 입사 
    emp_2 = Employee('Minjung', 'Kim', 60000)  # 직원 1명 입사
    print Employee.num_of_emps  # 직원 수 확인

    del emp_1  # 직원 1명 퇴사
    del emp_2  # 직원 1명 퇴사
    print Employee.num_of_emps  # 직원 수 확인
    ```
### 📖 Matrix Class

- A Matrix Class with Only Two Methods: Constructor + Print Method

    ```py
    class Matrix:
        def __init__(self, rows):
            self.e = rows
        def printMatrix(m):
            for row in m.e:
                rows = [str(e) for e in row]
                print(" ".join(rows))

    if __name__ == '__main__':
        m = Matrix([[0]*3 for i in range(2)])
        m.printMatrix()
    ```

- Checking the Contents of the Namespaces; **"dir"**

    ```py
    >>> dir(Matrix)

    >>> dir(m)
    ```

- Documentation Using Docstrings

    You may add a string just below the *def* line for Documentation

    ```py
    class Matrix:
        'a simple matrix class'
        def __init__(self, rows):
            'Matrix constructor'
            self.e = rows
        def printMatrix(self):
            'Print the elements in a matrix shape'
        def printMatrix(self):
            for row in self.e:
                rows = [str(e) for e in row]
                print(" ".join(rows))
    ```

### 📖 Special Method; __init__, __str__, __getitem__, __setitem__

<a href="https://corikachu.github.io/articles/python/python-magic-method">참고</a>

- __init__

    class의 구조를 결정

- __str__ & __repr__

    우리가 작성하는 클래스에서 str과 repr이 다른 결과를 반환하도록 하는 것이
    얼마든지 가능하다

    ```py
    class A:
        # __str__은 구현하지 않음 (다시말해 overriding 하지 않는다)
        def __repr__(self):
            return str(id(self))
    a = A()
    print(a)   # 140249540632704

    class NewInt(A, int):
        pass

    n = NewInt(5)
    print(n+5)  # 10 (int에서 상속받은 __add__메소드 호출)
    print(str(n))  # 5 (int에서 상속받은 __str__메소드 호출)
    print(repr(n))  # '140249540506184' (A에서 상속받은 __repr__메소드 호출 => n의 실제값이 아닌 고유한 메모리 주소값 반환)
    ```
    - NewInt클래스는 클래스A와 내장int자료형을 다중 상속받음(각각의 특징 유지)

    - <a href="https://shoark7.github.io/programming/python/difference-between-__repr__-vs-__str__">참고</a>

    - Example: Matrix

    ```py
    class Matrix:
        ...
        def __str__(self):
            rowstrs = []
            for row in self.e:
                rows = [str(n) for n in row]
                rowstrs.append(' ',join(rows))
            return '\n'.join(rowstrs)
    ```
- __getitem__(self, key) : indexing

    객체에서 []연산자를 사용하여 조회할때 동작을 정의한다. 예를들어 _list[10]은 _list.__getitem__(10)으로 동작한다.
    키의 타입이 적절하지 않다면 TypeError에러를, 키가 인덱스를 벗어났을 경우는 IndexError를 던져야 한다

- __setitem__(self, key, value) : indexing

    객체에서 []연산자를 사용해서 변수를 지정할 때 동작을 정의한다. 예를들어 +list[10] = 1은 _list.__setitem__(10, 1)으로 동작한다



