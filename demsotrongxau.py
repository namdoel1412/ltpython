t = int(input())
for i in range(0, t):
    inp = input()
    n = input()
    length1 = len(inp)
    length2 = len(n)
    res = 0
    j = 0
    while j < length1:
        tmp = ''
        for k in range(0, length2):
            if j+k < length1:
                tmp += inp[j+k]
        if tmp == n:
            res += 1
            # print(j)
            # print(tmp)
            j+=length2
        else:
            j+=1
            
    print(res)