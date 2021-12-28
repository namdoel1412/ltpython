n = int(input())
lst = [int(i) for i in input().split()]
dic = {}
for i in lst:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i]+=1

for i in range(1, n+2):
    if i not in dic:
        print(i)
        break
