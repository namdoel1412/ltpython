t = int(input())

def checkvalid(inp):
    length = len(inp)
    if length < 3:
        return False
    res = -1
    for i in range(0, length-1):
        if inp[i] >= inp[i+1]:
            res = i
            break
    if res == -1:
        return False
    for i in range(res, length-1):
        if inp[i] <= inp[i+1]:
            return False
    return True



for i in range(0, t):
    n = input()
    if checkvalid(n):
        print('YES')
    else:
        print('NO')