def getsum(inp):
    res = 0
    for i in inp:
        res += int(i)
    return res

def isPrime(inp):
    tmp = int(inp**0.5)
    for i in range(2, tmp+1):
        if(inp%i==0):
            return False
    return True
    

n = int(input())
for i in range(0, n):
    num = input()
    if(isPrime(getsum(num))):
        print('YES')
    else:
        print('NO')

