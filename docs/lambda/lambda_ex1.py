if __name__ == '__main__':
    Arr1 = [1, 2, 3, 4, 5, 6, 7]
    Arr2 = [8, 9, 10, 11, 12, 13, 14]

    outArr1 = list(map(lambda x: 'OK' if x%2==0 else x*x, Arr1))
    print('outArr1:', outArr1)

    outArr2 = list(map(lambda x: 'First' if x==1 else 'Second' if x==2 else x*x, Arr1))
    print('outArr2:', outArr2)

    outArr3 = list(map(lambda x, y: x+y, Arr1, Arr2))
    print('outArr3:', outArr3)