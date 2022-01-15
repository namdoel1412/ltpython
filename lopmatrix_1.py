t = int(input())
for i in range(0, t):
    lst = [int(i) for i in input().split()]
    n = lst[0]
    m = lst[1]
    matrix = []
    for j in range(0, n):
        tmp = [int(i) for i in input().split()]
        matrix.append(tmp)
    for j in range(0, n):
        for h in range(0, n):
            tmp = 0
            for k in range(0, m):
                tmp += matrix[j][k]*matrix[h][k]
            print(tmp, end=' ')
        print()

