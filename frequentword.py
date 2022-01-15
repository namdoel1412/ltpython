n = int(input())
dic = {}
for i in range(0, n):
    lst = input().split()
    for item in lst:
        if item not in dic:
            dic[item]=1
        else:
            dic[item]+=1
# print(dic.items())
lst2 = sorted(dic.items(), key= lambda x : x[1], reverse=True)
# print(lst2)
res = []
length = len(lst2)
check = 0
for i in range(0, length-1):
    if(check == 1):
        res.append(lst2[i][0])
    if lst2[i][1] != lst2[i+1][1]:
        check+=1
    if check > 1:
        break
res = sorted(res)
for item in res:
    print(item, end=' ')
print()
