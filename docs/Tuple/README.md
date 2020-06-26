# Tuple

list와 거의 비슷하지만 변경 불가능(Immutable)한 특성을 가짐

슬라이스와 인덱싱은 지원하지만 append, pop, remove는 지원X

즉, 값의 추가, 수정, 삭제 불가능

## 📙 contents

1. 문법
2. Packing/Unpacking
3. Swap
4. Set
5. 합집합, 교집합, 차집합, 여집합의 연산

### 📖 문법

```py
number = (1, 2, 3, 4, 5)
```

- Tuple 인덱싱

    ```py
    tu1 = (1, 2, 'a', 'b')
    # 0번째 값: 1
    # 3번째 값: b
    ```

- Tuple 슬라이싱

    ```py
    tu1[0:]  #0번째 부터
    tu1[0:2]  #0번째 부터 2번째까지
    ```

- Tuple끼리 더하기

    ```py
    tu1 = (1, 2, 'a', 'b')
    tu2 = (3, 4, 'c', 'd')
    tu1 + tu2
    # (1, 2, 'a', 'b', 3, 4, 'c', 'd')
    ```

- Tuple 곱하기

    ```py
    tu1 = (1, 2, 3, 4)
    tu1 * 3
    # (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
    ```



### 📖 Packing / Unpacking

- Packing: 하나의 변수에 여러개의 값을 집어넣는 것

    ```py
    numbers = (1,2,3,4,5,6,7)
    ```

- Unpacking: 패킹된 변수에서 여러개의 값을 가져오는 것

    ```py
    (a, b, c, d, e, f, g) = numbers
    # a = 1, g = 7
    ```

    Packing과 Unpacking의 갯수를 맞춰야한다!

- 슬라이싱을 통해 원하는 부분만 Unpacking가능

    ```py
    numbers = (55, 33, 11)
    (vv1, vv2, vv3) = numbers[-3:]
    (v1, v2, v3, v4, v5, v6, v7) = (*numbers, 1, 2, 4, 5)
    ```

### 📖 Swap

```py
x, y = 1, 2
x, y = y, x
# y = 1, x = 2
```
Java나 C의 경우 x,y를 바꾸려면 temp사용

파이썬은 간단히 x,y = y,x 한줄로 바꿀 수 있다

### 📖 Set

중복을 허용하지 않는 데이터의 집합

list에서 중복을 제거하려 할 때 set을 사용할 수 있다

set은 추가된 순서를 유지하지X

```py
number = {1,1,1,1,2,2,2,2,2,4,5,8}
list(set(number))
# [1,2,4,5,8]
```

### 📖 합집합, 교집합, 차집합, 여집합의 연산

```py
num1 = {1,2,3,4,5}
num2 = {3,4,5,6,7}

num1-num2   #차집합: {1,2}
num1|num2   #합집합: {1,2,3,4,5,6,7}
num1&num2   #교집합: {3,4,5}
num1^num2   #여집합: {1,2,6,7}
```

