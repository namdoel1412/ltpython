n = int(input())
matrix = []
halfTop = 0
halfBottom = 0
for i in range(0, n):
    lst = [int(i) for i in input().split()]
    matrix.append(lst)
    for j in range(0, n-i-1):
        halfTop += lst[j]
    for j in range(n-1, n-i-1, -1):
        halfBottom += lst[j]
k = int(input())
# print(halfTop)
# print(halfBottom)
res = abs(halfTop-halfBottom)
if abs(halfTop-halfBottom) <= k:
    print('YES')
else:
    print('NO')
print(res)