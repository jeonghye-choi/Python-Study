# Comprehending Data Structures

## 📙 contents

1. Designing a Data Structure; Matrix
2. List Comprehension
3. Nested Loops
4. Loops and Functions

### 📖 Matrix

행렬 -> 프로그래밍에서, 데이터를 저장하는데 사용

- List
    [[2, 4], [1, 3]]
- tuple
    ((2, 4), (1, 3))

- Making Matrix; Using Loops(list append method)

    ```py
    m1 = []
    for i in range(3):
        m1.append([])
        for j in range(3):
            m1[i].append(i+j)
    print(m1)

    # [[0,1,2], [1,2,3], [2,3,4]]
    ```

### 📖 List Comprehension (조건제시법)

[2*n for n in range(10)]
[2**n for n in range(10)]

- Making Matrix; Using List Comprehension

    ```py
    m2 = [[i+j for j in range(3)] for i in range(3)]
    print(m2)
    ```
- 한변의 길이가 짝수인 정사각형의 넓이출력; Using List Comprehension

    ```py
    [i*i for i in range(1,5) if i%2 == 0]
    ```

- 좌표출력; Using List Comprehension

    ```py
    [(x,y) for x in range(5) for y in range(5)]

    # [(0,0), (0,1), (0,2), ... ,(4,4)]
    ```

- Dictionary Comprehension

    ```py
    student = ["Kim", "Lee", "Park", "Choi"]
    {f"{number}" : name for number, name in enumerate(student)}
    # {'0': 'Kim', '1': 'Lee', '2': 'Park', '3': 'Choi'}

    {f"{number}" : name for number, name in enumerate(student)}
    # {'1': 'Kim', '2': 'Lee', '3': 'Park', '4': 'Choi'}
    ```

- Dictionary Comprehension; Using *zip*

    ```py
    A = ["male", "dad", "man"]
    B = ["female", "mom", "woman"]
    result = {A:B for A, B in zip(A,B)}
    # {'male': 'female', 'dad': 'mom', 'man': 'woman'}
    ```

### 📖 Nested Loops

A loop of a loop is called a nested loop

Input: a matrix and a list

output: initialize the matrix

- Example: Matrix Initialization

    ```py
    def main():
        row = 2
        col = 3
        mat = [[0]*col for i in range(row)]
        print(mat)
        initlist = [1, 9, -12, 20, -5, 7]
        k = 0
        for i in range(row):
            for j in range(col):
                mat[i][j] = initlist[k]
                k += 1
        print(mat)

    if __name__ == '__main__':
        main()
    ```

- Example: Filtering Negative

    ```py
    def filter_neg(mat):
        row = len(mat)
        col = len(mat[0])
        mat2 = [[0]*col for i in range(row)]
        for i in range(row):
            for j in range(col):
                if mat[i][j] < 0:
                    mat2[i][j] = 0
                else:
                    mat2[i][j] = mat[i][j]
        return mat2
    ```
- Example: Transpose
    ![image](https://user-images.githubusercontent.com/54584063/85838613-cab48780-b7d4-11ea-90c3-a192ed40bc05.png)

    ```py
    def transpose(mat):
        row = len(mat)
        col = len(mat[0])
        mat2 = [[0]*row for i in range(col)]
        for i in range(row):
            for j in range(col):
                mat2[j][i] = mat[i][j]
        return mat2
    ```
- Example: Matrix Multiplication

    ```py
    def product(m1, m2):
        row1 = len(m1)
        col1 = len(m1[0])
        row2 = len(m2)
        col2 = len(m2[0])
        assert col1 == row2
        mat = [[0]*row1 for i in range(col2)]
        for i in range(row1):
            for j in range(col2):
                mat[i][j] = 0
                for k in range(col1):
                    mat[i][j] += m1[i][k] * m2[k][j]
        return mat
    ```

### 📖 Loops and Functions

- Too Much Nesting -> Reduce; function

    ```py
    def iproduct(v1, v2):
        p = 0
        for i in range(len(v1)):
            p += v1[i] * v2[i]
        return p

    def rowvec(m, i):
        v = [m[i][j] for j in range(len(m[0]))]
        return v
    def colvec(m, j):
        v = [m[i][j] for i in range(len(m))]
        return v
    ```

- *numpy* Module; provide powerful matrix operations

    ```py
    ms = [ns[s:s+3] for s in range(0, 10, 3)]
    mt = [[1,1] for _ in range(3)]
    
    import numpy as np
    m1 = np.matrix(ms)
    print(m1)
    m2 = np.matrix(mt)
    m3 = m1 * m2
    ```

    You can see the various operations useing *help*
    
    ```py
    >>> help(np.matrix)
    ```

- Dictionary Comprehension

    ```py
    ls = ['one', 'two', 'three', 'four']
    val = {name:i+1 for (i, name) in enumerate(ls)}
    print(val)

    # {'three':3, 'two':2, 'four':4, 'one':1}
    ```

    ```py
    db1 = {k:v*2 for (k,v) in val.items()}
    print(db1)

    # {'one':2, 'four':8, 'two':4, 'three':6}
    ```