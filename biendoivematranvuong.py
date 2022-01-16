lst = [int(i) for i in input().split()]
N = lst[0]
M = lst[1]
matrix = []
for i in range(0, N):
    tmp = [int(j) for j in input().split()]
    matrix.append(tmp)

if N > M:
    step = N - M
    for i in range(0, step):
        matrix.pop(i)
elif M > N:
    step = M - N
    for i in range(0, N):
        for j in range(0, step):
            matrix[i].pop(j+1)

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
