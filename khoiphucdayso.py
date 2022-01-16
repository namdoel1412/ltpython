t = int(input())
matrix = []
for i in range(0, t):
    lst = [int(i) for i in input().split()]
    matrix.append(lst)

res = [0 for i in range(0, t)]

if t == 2:
    print('1 1')
else:
    z = matrix[t-2][t-1]
    y = matrix[t-3][t-1]
    x = matrix[t-3][t-2]
    #print(x, y, z)
    final = int((y-x+z)/2)
    #print(final)
    res[t-1] = final
    for j in range(0, t-1):
        res[j] = matrix[t-1][j] - final
    for j in range(0, t):
        print(res[j], end=' ')


