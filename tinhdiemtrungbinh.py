n = int(input())
lst = [float(i) for i in input().split()]
lst = sorted(lst)
length = len(lst)
sum = 0
count = 0
for i in range(1, length-1):
    if lst[i] != lst[0] and lst[i] != lst[length-1]:
        sum+=lst[i]
        count+=1
res = round(sum/count, 2)
print(res)