# Recursion 재귀함수

- 함수 정의 내에 같은 이름의 함수가 올 때 이를 재귀함수라 부른다

- 반드시 탈출조건이 있어야 stack overflow를 방지할 수 있다

- 같은 행위가 반복될 때 재귀함수를 사용한다

### 📖 Example

- 순차탐색

    ```py
    def search(li, begin, end, target):
        if begin>end:
            return -1
        elif target == li[begin]:
            return begin
        else:
            return search(li, begin+1, end, target)

    li = [1,6,10,7,2,5]
    print(search(li, 0, 5, 10))   #2
    ```

- 2진수 변환

    ```py
    def print_binary(n):
        if n<2:
            print(n, end='')
        else:
            print_binary(n//2)
            print(n%2, end='')

    print_binary(15)
    ```

- 배열의 합

    - li[0]에서 li[n-1]까지의 합을 구하여 리턴

    - 재귀적 사고방식: li[n-1] + (li[n-2]까지의 합)을 구한다

    ```py
    def sum(n, li):
        if n<=0 or n>=len(li):
            return 0
        return li[n-1] + sum(n-1, li)

    print(sum(3, [1,2,3,4,5,6,7]))   #6
    ```

- 0~n까지의 합계 구하기

    ```py
    def sum(n):
        if n == 0:
            return 0
        return n + sum(n-1)

    print(sum(4))   #10
    ```

- 0~n까지의 곱 구하기

    ```py
    def factorial(n):
        if n==1:
            return 1

        return n*factorial(n-1)

    print(factorial(4))   #24
    ```

- X^n 구현

    ```py
    def power(x, n):
        if n == 0:
            return 1
        return x*power(x, n-1)

    print(power(2, 10))   #1024
    ```

- 피보나치 수열

    ```py
    def fibo(n):
        if n ==1 or n==0:
            return 1

        return fibo(n-1) + fibo(n-2)

    def fibo_list(n):
        for i in range(n):
            print(fibo(i), end=" ")

    fibo_list(5)   # 1 1 2 3 5 
    ```

- 최대공약수 (유클리드 호제법)

    ```py
    def gcd(m, n):
        if m < n:
            m, n = n, m
        if m % n == 0:
            return n
        else:
            return gcd(m, m%n)
    print(gcd(48, 60))   #12
    ```

- 하노이타워

    ```py
    def hanoi(num, _from, _by, _to):
        #탈출 조건
        if num == 1:
            print("{}에서 {}로 {} 번째 원반 이동".format(_from, _to, num))
            return

        hanoi(num-1, _from, _to, _by)
        print("{}에서 {}로 {} 번째 원반 이동".format(_from, _to, num))
        hanoi(num-1, _by, _from, _to)

    if __name__ == "__main__":
        while 1:
            numOfTray = int(input("원반의 개수를 입력하세요!(종료 : 0) :"))
            if numOfTray == 0:
                break
            hanoi(numOfTray, 'A', 'B', 'C')
    ```

