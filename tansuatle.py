t = int(input())
for i in range(0, t):
    dic = {}
    n = int(input())
    lst = [int(i) for i in input().split()]
    lst = sorted(lst)
    for j in range(0, n):
        if lst[j] not in dic:
            dic[lst[j]] = 1
        else:
            dic[lst[j]]+=1
    for item in dic.keys():
        if dic[item]%2!=0:
            print(item)
            break