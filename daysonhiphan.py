n = int(input())
lst = [int(i) for i in input().split()]
length = len(lst)
res = 0
for i in range(0, length-1):
    if lst[i] != lst[i+1]:
        res+=1
print(res)