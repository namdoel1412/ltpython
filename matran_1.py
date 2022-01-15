n = int(input())
top = 0
down = 0
for i in range(0, n):
    lst = [int(i) for i in input().split()]
    for j in range(0, n):
        if j > i:
            top += lst[j]
        elif j < i:
            down += lst[j]
k = int(input())
# print(top)
# print(down)
dis = abs(top - down)
if dis <= k:
    print('YES')
else:
    print('NO')
print(dis)

