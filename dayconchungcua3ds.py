t = int(input())
for i in range(0, t):
    dic1 = {}
    dic2 = {}
    dic3 = {}
    lst = [int(j) for j in input().split()]
    lst1 = [int(j) for j in input().split()]
    lst2 = [int(j) for j in input().split()]
    lst3 = [int(j) for j in input().split()]
    for item in lst1:
        if item not in dic1:
            dic1[item] = 1
        else:
            dic1[item] += 1

    for item in lst2:
        if item not in dic2:
            dic2[item] = 1
        else:
            dic2[item] += 1

    for item in lst3:
        if item not in dic3:
            dic3[item] = 1
        else:
            dic3[item] += 1
    
    res = True
    for item in lst1:
        if (item in dic1 and item in dic2 and item in dic3) and (dic1[item] > 0) and (dic2[item] > 0) and (dic3[item] > 0):
            print(item, end=' ')
            dic1[item]-=1
            dic2[item]-=1
            dic3[item]-=1
            res = False
    if res == True:
        print('NO', end='')
    print()
    
