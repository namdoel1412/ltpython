def getsum(str):
    res = 1
    for i in str:
        res *= int(i)
    return res

def compare(str1, str2):
    if getsum(str1) < getsum(str2):
        return 1
    elif getsum(str1) == getsum(str2) and str1 < str2:
        return 1
    return 0

test = int(input())
for i in range(0, test):
    n = int(input())
    lst = [int(i) for i in input().split()]
    tmp = sorted(lst)
    # for k in tmp:
    #     print(k, end=' ')
    # print()
    lstStr = [str(i) for i in tmp]
    newlist = sorted(lstStr, key=getsum)
    for j in newlist:
        print(j, end=' ')
    print()

