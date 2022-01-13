def tich_tong(inp):
    length = len(inp)
    lst = []
    lst.append(1)
    lst.append(0)
    flag = True
    for i in range(0, length):
        if i%2 == 0:
            if(inp[i] != '0'):
                lst[0] *= int(inp[i])
                flag = False
        else:
            lst[1] += int(inp[i])
    if flag:
        lst[0] = 0
    return lst

n = int(input())
for i in range(0, n):
    inp = input()
    res = tich_tong(inp)
    print(res[0], end=' ')
    print(res[1])

