n = int(input())
top = 0
down = 0
for i in range(0, n):
    lst = [int(j) for j in input().split()]
    for j in range(0, n):
        if j < n-i-1:
            top+=lst[j]
        elif j > n-i-1:
            down+=lst[j]
value = abs(top-down)
k = int(input())
if value <= k:
    print('YES')
else:
    print('NO')
print(value)

