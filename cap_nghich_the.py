n = int(input())
lst = []
arr = input()
lst = arr.split(' ', -1)
for i in range(0, n):
    lst[i] = int(lst[i])
res = 0
for i in range(0, n-1):
    for j in range(i+1, n):
        if lst[i] > lst[j]:
            res+=1
print(res)