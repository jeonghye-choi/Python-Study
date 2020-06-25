from functools import reduce

if __name__=='__main__':
    Arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    outArr1 = list(filter(lambda x: x>5 and x<15, Arr))
    print('Lambda Filter ex1:', outArr1)

    outArr2 = reduce(lambda x,y: x+y, Arr)
    print('Lambda Reduce ex2:', outArr2)