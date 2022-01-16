t = int(input())
for i in range(0, t):
    n = int(input())
    lstA = [int(j) for j in input().split()]
    lstB = [int(j) for j in input().split()]
    lstA = sorted(lstA)
    lstB = sorted(lstB)
    check = True
    for j in range(0, n):
        if lstA[j] > lstB[j]:
            check = False
            break
    if check == True:
        print('YES')
    else:
        print('NO')
    