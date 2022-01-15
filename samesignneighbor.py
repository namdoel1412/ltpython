n = int(input())
res = 0
a = 0
b = 0
#for i in range(0, n):
lst = [int(i) for i in input().split()]
length = len(lst)
for j in range(0, length-1):
    if lst[j]*lst[j+1] > 0:
        res +=1
        a = lst[j]
        b = lst[j+1]
if res == 0:
    print(0)
else:
    print(res , end=' ')
    print(a, end=' ')
    print(b)