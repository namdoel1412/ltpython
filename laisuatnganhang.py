t = int(input())
for i in range(t):
    req = input().split()
    N = float(req[0])
    X = float(req[1])
    M = float(req[2])
    # print(N, X, M)
    vt = M/N
    vp = 1+X/100
    # print(vt, vp)
    i = int(vt)
    while(True):
        if vt <= vp**i:
            break
        i+=1
    if i - int(i) > 0:
        i+=1
    print(int(i))

    


