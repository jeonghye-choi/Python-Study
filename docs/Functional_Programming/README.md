# Functional Programming

## 📙 contents

1. Data Structure
2. Algorithm; How to Solve the Problem
3. Programming Style and Functional Programming

### 📖 Data Structure

자료구조는 자료를 효율적으로 이용할 수 있도록 컴퓨터에 저장하는 방법

- 자료구조를 사용하는 이유

    자료를 더 효율적으로 저장, 관리하기 위해서

    실행시간단축과 메모리용량의 절약

- 파이썬 자료구조의 종류

    리스트(list), 튜플(tuple), 사전(dict) 형태가 가장 많이 사용됨

### 📖 Algorithm

Algorithm: a finite sequence of definite computational steps to solve the problem

should be definite and considered as a unit task

- Selecting a good representation of data

    1. easy to manipulate
    2. compact enough to be stored in the computer memory


- Problem Soving Steps

    1. specific
    2. design (representation of data, devise algorithm)
    3. implement as a code
    4. test and modify

- How to transform the Input

    1. copying (duplicating) the data
    2. deleting the data
    3. reordering the data
    4. making a new data

### 📖 Programming Style

- imperative (control-oriented)

    : sequence of commands

- functional (value-oriented)

    : function applications

    ```py
    # Imperative Style
    def charlist(str):
        list = []
        for c in str:
            list.append(c)
        list.sort()
        return list
    
    # Functional Style
    def charlist(str):
        list = list(str)
        list.sort()
        return list
    ```