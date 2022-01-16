inp = input()
length = len(inp)
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
for item in dic.keys():
    print(item, end=' ')
    print(dic[item])