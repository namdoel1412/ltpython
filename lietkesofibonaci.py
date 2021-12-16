t = int(input())
for i in range(t):
    line = [int(j) for j in input().split()]
    a = line[0]
    b = line[1]
    lst = []
    lst.append(1)
    lst.append(1)
    for k in range(1, b+1):
        tmp = lst[k]+lst[k-1]
        lst.append(tmp)
    for k in range(a, b+1):
        print(lst[k-1], end=' ')
    print()