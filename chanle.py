t = int(input())
for i in range(t):
    req = input()
    length = len(req)
    sum = int(req[length-1])
    res = True
    for j in range(length-1):
        tmp = int(req[j])
        if abs(tmp - int(req[j+1])) != 2:
            res = False
            break
        sum += tmp
    if res == False:
        print('NO')
    else:
        if sum%10==0:
            print('YES')
        else:
            print('NO')

