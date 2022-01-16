t = int(input())
top = 0
down = 0
for i in range(0, t):
    lst = [int(j) for j in input().split()]
    for j in range(i+1, t):
        top += lst[j]
    for j in range(0, i):
        down += lst[j]
k = int(input())
res = abs(top-down)
if res <= k:
    print('YES')
else:
    print('NO')
print(res)