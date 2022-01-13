t = int(input())
for i in range(0, t):
    S = 0
    N = int(input())
    if N%2!=0:
        for j in range(1, N+1, 2):
            S += 1/j
    else:
        for j in range(2, N+1, 2):
            S += 1/j
    res = round(S, 6)
    tmp = str(res)
    length = len(tmp)
    for j in range(0, length):
        if(tmp[j] == '.'):
            res = 0
        else:
            res+=1
    if res < 6:
        for j in range(0, 6-res):
            tmp+='0'
    print(tmp)
