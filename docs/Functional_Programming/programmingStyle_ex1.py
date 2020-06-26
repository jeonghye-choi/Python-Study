def wfamily(w1, w2):
    for c in w1:
        w2 = w2.replace(c, "")
    # if w2 == "":
    #     return "YES"
    # else:
    #     return "NO"
    return "YES" if w2 == "" else "NO"
    

def wfamily2(w1, w2):
    l1 = []
    for c in w1:
        l1.append(c)
    l1.sort()

    l2 = list(w2)
    l2.sort()
    
    return "YES" if l1 == l2 else "NO"

if __name__ == '__main__':
    w1 = "lotofsons"
    w2 = "lost"
    ans = wfamily2(w1, w2)
    print(ans)

    w1 = "lots"
    ans = wfamily2(w1, w2)
    print(ans)