t = int(input())
dic = {}
num = 0
for i in range(0, t):
    lst = input().split()
    num += len(lst)
    for j in lst:
        if j not in dic:
            dic[j] = 1
        else:
            dic[j]+=1

lst = sorted(sorted(dic.items(), key = lambda x : x[0]), key= lambda x : x[1], reverse=True)
for item in lst:
    print(item[0], end=' ')
    print(round(item[1]/num, 2))
