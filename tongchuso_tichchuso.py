def check(tmp):
    length = len(tmp)
    res = []
    res.append(0)
    res.append(1)
    all_zero = True
    for j in range(0, length):
        if(j%2==0):
            res[0]+=int(tmp[j])
        else:
            if int(tmp[j]) != 0:
                res[1]*=int(tmp[j])
                all_zero = False
    if all_zero:
        res[1] = 0
    return res


n = int(input())
for i in range(0, n):
    tmp = input()
    res = check(tmp)
    print(res[0], end=' ')
    print(res[1])
