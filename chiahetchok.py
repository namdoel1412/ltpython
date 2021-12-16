lst = [int(x) for x in input().split()]
a = lst[0]
K = lst[1]
N = lst[2]

limit = int(N/K)
check = True
for i in range(1, limit+1):
    if K*i <= N and K*i-a > 0:
        check = False
        print(K*i - a, end=' ')

if check == True:
    print(-1)