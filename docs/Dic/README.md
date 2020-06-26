# Diction 사전형

Key와 Value의 쌍으로 구성된 집합

Key는 고유값이며 중복 허용X

{key1:value1, key2:value2, key3:value3, ...}

### 📖 사전의 사용

- value 값 체크가능?: No!

    ```py
    example = {'key1':10, 'key2':5, 'key3':1}
    print(10 in example) #False
    ```
- key값으로 체크가능?: Yes!

    ```py
    example = {'key1':10, 'key2':5, 'key3':1}
    print(key1 in example) #True
    ```

- 키 값만 불러오기

    ```py
    example = {'key1':10, 'key2':5, 'key3':1}
    for key in example:
        print(key)   #key1 key2 key3
    ```

- 값 불러오기

    ```py
    example = {'key1':10, 'key2':5, 'key3':1}
    for value in example.values():
        print(value)   #10 5 1
    ```

- 키와 값 둘다 불러오기: item()

    ```py
    example = {'key1':10, 'key2':5, 'key3':1}
    for (key, value) in example.items():
        print(key, value)
    ```

- 값(value)변경

    ```py
    example = {'key1':10, 'key2':5, 'key3':1}
    example['key1'] = 90
    ```

- 새로운 Key:Value 등록

    ```py
    example['key_new'] = 40
    ```

- Key:Value 제거

    ```py
    del example['key1']
    ```
    없는 key를 제거 -> KeyError