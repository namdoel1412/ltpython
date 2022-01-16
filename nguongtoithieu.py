inp = input()
length = len(inp)
k = int(input())
if length % 2 != 0:
    inp = inp[:-1]
    length-=1
res = []
dic = {}
for i in range(0, length-1, 2):
    tmp = int(inp[i]+inp[i+1])
    if tmp not in dic:
        dic[tmp] = 1
    else:
        dic[tmp]+=1
res = sorted(dic.items())
check = True
for item in res:
    if item[1] >= k:
        print(item[0], end=' ')
        print(item[1])
        check = False
if check == True:
    print('NOT FOUND')