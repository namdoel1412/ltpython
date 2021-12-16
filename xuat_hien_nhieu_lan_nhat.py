t = int(input())
for i in range(0, t):
    n = int(input())
    lst = []
    str = input()
    lst = str.split(' ', -1)
    minn = 2000000
    cmp = n/2
    for j in range(0, n):
        lst[j] = int(lst[j])
    for j in range(0, n):
        if lst[j] < minn and lst.count(lst[j]) > cmp:
            minn = lst[j]
    if minn == 2000000:
        print('NO')
    else:
        print(minn)
