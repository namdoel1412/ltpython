from cmath import inf


t = int(input())
lst = [int(i) for i in input().split()]

minn = inf
value = -1
for i in range(0, t-1):
    res = 0
    for j in range(0, t):
        res += abs(lst[i] - lst[j])
    if minn > res:
        value = lst[i]
        minn = res

print(minn, end=' ')
print(value)
    
    