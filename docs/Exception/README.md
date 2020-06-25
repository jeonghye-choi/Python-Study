# Exceptions (예외처리)

## 📙 contents

1. [Exception Handling](###📖-Exception-Handling)

2. ["else" clause](###📖-"else"-clause)

3. ["finally" clause](###📖-"finally"-clause)

4. [User-Defined Exceptions](###📖-User-Defined-Exceptions)

### 📖 Exception Handling

- #### Example: ZeroDivisionError

    ```py
    line = input()
    amount = sum(map(ord, line))  # ord(): 아스키코드로 바꿔줌
    number = len(line)

    try:
        share = amount/number
    except:
        print("Divider zero is ignored")
    ```

- #### Example: ValueError

    ```py
    # wrongly
    try:
        amount = int(input())
        share = amount/number
    except:
        print("Divider zero is ignored")

    # target exception can be specified in an except clause
    try:
        amount = int(input())
        share = amount/number
    except ZeroDivisionError:
        print("Divider zero is ignored")
    ```
- #### Example: Multiple Exception

    ```py
    try:
        amount = int(input("Enter the amount: "))
        number = int(input("ENter the number of persons: "))
        share = amount/number
    except ZeroDivisionError:
        print("Divider zero is ignored")
    except ValueError:
        print("Incorrect value is not processed")
    except Exception:
        print("Unidentified error is occurred")
    ```


### 📖 "else" clause

- #### Example: else

    ```py
    fname = input("Enter the file name")
    try:
        fin = open(fname, 'r')
    except FileNotFountError:
        print(f"Error: cannot open '{fname}'")
    else:
        lines = fin.readlines()
        print(f"'{fname}' contains {len(lines)} lines")
        fin.close()
    ```
### 📖 "finally" clause

마지막에 무조건 실행

try(성공)->else->finally
try(실패)->except->finally

- #### Example: finally
    ```py
    fname = input("Enter the file name")
    try:
        fin = open(fname, 'r')
    except FileNotFountError:
        print(f"Error: cannot open '{fname}'")
    else:
        lines = fin.readlines()
        print(f"'{fname}' contains {len(lines)} lines")
        fin.close()
    finally:
        print("Thanks for using this program!")
    ```

### 📖 User-Defined Exceptions

자신만의 예외 계층을 구축가능

대형 모듈을 작성할 때 유용하다!

- #### Example: Defining User-Defined Exception

    ```py
    class PNUError(Exception):
        ...

    class DBError(PNUError):
        ...

    class IOError(PNUError):
        ...
    ```
- #### Example: Raising Exceptions with raise

    ```py
    raise NameError('What?')
    ```

- #### Naming an Exception with "as"

    ```py
    except OSError as err:
        print(f"OS error: {error}")
    ```

- #### with Statement

    with을 사용하면 파일을 열었을 때 자동으로 닫힌다!

    ```py
    with open("myfile.txt") as f:
        for line in f:
            print(line, end="")
    ```



