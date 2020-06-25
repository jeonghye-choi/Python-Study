def incr(count, gamma=1, delta=2):
    print(f"{count}. gamma: {gamma}, delta: {delta}")

if __name__ == '__main__':
    incr(1)  #1. gamma: 1, delta: 2
    incr(2,2)  #2. gamma: 2, delta: 2
    incr(3,2,1)  #3. gamma: 2, delta: 1
    incr(4, delta=5)  #4. gamma: 1, delta: 5