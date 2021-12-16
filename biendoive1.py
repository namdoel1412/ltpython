while True:
    N = int(input())
    if N == 0:
        break
    res = 1
    while N != 1:
        res+=1
        #print(N, end=' ')
        if N%2 == 0:
            N = int(N/2)
        else:
            N = N*3 + 1
    print(res)
