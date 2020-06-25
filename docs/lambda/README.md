# lambda 람다식

'lambda'는 런타임에 생성해서 사용할 수 있는 익명함수

**lambda 인자리스트: 표현식**

- lambda 매개변수1, 매개변수2, ... : 출력식1 if 조건문 else 출력식2

## 📙 contents

1. lambda + map()

2. lambda + filter()

3. lambda + reduce()

### 📖 lambda + map

map(function, iterable, ...)

```py
# lambda_ex1.py

if __name__ == '__main__':
    Arr1 = [1, 2, 3, 4, 5, 6, 7]
    Arr2 = [8, 9, 10, 11, 12, 13, 14]

    # 예제1
    outArr1 = list(map(lambda x: 'OK' if x%2==0 else x*x, Arr1))
    print('outArr1:', outArr1)

    # 예제2: 다중 조건식은 가독성이 떨어짐 -> 되도록 함수로 분리
    outArr2 = list(map(lambda x: 'First' if x==1 else 'Second' if x==2 else x*x, Arr1))
    print('outArr2:', outArr2)

    # 예제3: 다중 매개변수 map + 람다식 활용
    outArr3 = list(map(lambda x, y: x+y, Arr1, Arr2))
    print('outArr3:', outArr3)
```

### 📖 lambda + filter

**filter(function, iterable)**

function은 처리되는 각각의 요소에 대해 Boolean 값을 반환

True를 반환하면 그 요소는 남게 되고, False를 반환하면 그 요소는 제거된다

```py
# lambda_ex2.py
if __name__=='__main__':
    Arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    outArr1 = list(filter(lambda x: x>5 and x<15, Arr))
    print('Lambda Filter ex1:', outArr1)

    ## Lambda Filter ex1: [6, 8, 10, 12, 14]
```

### 📖 lambda + reduce

**functools.reduce(function, iterable[, initializer])**

첫 번째 인덱스의 요소부터 순차적으로 정의된 함수로 처리

예를 들어 reduce(function, [1,2,3,4,5]) 에서 list 는 [function(1,2),3,4,5] 로 하나의 요소가 줄고, 요소가 하나가 남을 때까지 reduce(function, [function(1,2),3,4,5]) 를 반복



```py
# lambda_ex2.py
from functools import reduce

if __name__=='__main__':
    Arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    outArr2 = reduce(lambda x,y: x+y, Arr)
    print('Lambda Reduce ex2:', outArr2)

    ## Lambda Reduce ex2: 110
```
