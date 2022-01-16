lst = [int(i) for i in input().split()]
lst2 = [int(i) for i in input().split()]
dic = {}
for item in lst2:
    if item not in dic:
        dic[item] = 1
    else:
        dic[item] += 1
    
res = sorted(sorted(dic.items(), key=lambda x:x[0]), key=lambda x:x[1], reverse=True)
length = len(res)
result = -1
for i in range(0, length-1):
    if res[i][1] != res[i+1][1]:
        result = res[i+1][0]
        break
if result == -1:
    print('NONE')
else:
    print(result)