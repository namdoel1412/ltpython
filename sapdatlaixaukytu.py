n = int(input())
for i in range(0, n):
    inp1 = input()
    inp2 = input()
    
    dic1 = {}
    dic2 = {}

    for item in inp1:
        if item not in dic1:
            dic1[item]=1
        else:
            dic1[item]+=1
    
    for item in inp2:
        if item not in dic2:
            dic2[item]=1
        else:
            dic2[item]+=1
    res = True
    for item in dic1.keys():
        if (item not in dic2) or (item in dic2 and dic1[item] != dic2[item]):
            res = False
            break
    print('Test ' + str(i+1) + ': ', end='')
    if res:
        print('YES')
    else:
        print('NO')
