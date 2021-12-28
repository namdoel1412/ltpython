test = int(input())
for j in range(0, test):
    n = int(input())
    dic = {}
    for i in range(0, n):
        tmp = int(input())
        if tmp not in dic:
            dic[tmp]=1
        else:
            dic[tmp]+=1

    minn = 2000
    x = 0
    for i in dic.keys():
        # print(i, end=' ')
        # print(dic[i])
        if dic[i] > x:
            x = dic[i]
            minn = i
        elif dic[i] == x and i < minn:
            minn = i

    print(minn)

