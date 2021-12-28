def getsum(inp):
    res = 0
    for i in inp:
        res += int(i)
    return res

def checktn(inp):
    if inp < 10:
        return False
    tmp = str(inp)
    length = len(tmp)
    for i in range(0, int(length/2)):
        if(tmp[i] != tmp[length-i-1]):
            return False
    return True
    

n = int(input())
for i in range(0, n):
    num = input()
    if(checktn(getsum(num))):
        print('YES')
    else:
        print('NO')

