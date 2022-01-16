lst = [int(i) for i in input().split()]
lst1 = sorted(list(dict.fromkeys([int(i) for i in input().split()])))
lst2 = sorted(list(dict.fromkeys([int(i) for i in input().split()])))

length1 = len(lst1)
length2 = len(lst2)

if length1 != length2:
    print('NO')
else:
    res = True
    for i in range(0, length1):
        if lst1[i] != lst2[i]:
            res = False
            break
    if res:
        print('YES')
    else:
        print('NO')
