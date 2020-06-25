# Assertion (가정 설정문)

뒤의 조건이 True가 아니면 AssertError 발생

```py
a = 3
assert a == 2

#결과
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

함수의 성능을 높이기 위해 반드시 정수만을 입력받아 처리하도록 만들 수 있다. 이런 함수를
만들기 위해서는 반드시 함수에 정수만 들어오는지 확인할 필요가 있다. 이를 위해 if문을 사용할 수도 있고
'예외처리'를 사용할 수도 있지만 '가정 설정문'을 사용하는 방법도 있다

### 📖 example

- 정수인지 확인

    ```py
    lists = [1, 3, 6, 8, 7, 3.14, 1.3]

    def test(t):
        assert type(t) is int, '정수가 아닌 값이 있네'  #메세지 출력 가능
    
    for i in lists:
        test(i)

    #결과
    AssertError: 정수가 아닌 값이 있네
    ```
