def getsum(inp):
    length = len(inp)
    res = 1
    for i in range(0, length):
        if inp[i] != '0':
            res*=int(inp[i])
    return res

n = int(input())
for i in range(0, n):
    num = input()
    print(getsum(num))

    