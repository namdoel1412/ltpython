t = int(input())
for i in range(0, t):
    n = int(input())
    lst = [int(i) for i in input().split()]
    res = [(lst[0], 1)]
    print(1, end=' ')
    for j in range(1, n):
        tmp = 0
        while len(res) > 0 and res[len(res)-1][0] <= lst[j]:
            tmp += res[len(res)-1][1]
            res.pop()
        res.append((lst[j], tmp+1))
        print(tmp+1, end=' ')
    print()
    

