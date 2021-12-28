def check(inp):
    length = len(inp)
    for i in range(0, length):
        if i%2 == 0:
            if(int(inp[i])%2 != 0):
                return False
        else:
            if(int(inp[i])%2==0):
                return False
    return True

def getsum(inp):
    res = 0
    length = len(inp)
    for i in range(0, length):
        res += int(inp[i])
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
    if(check(num) and isPrime(getsum(num))):
        print('YES')
    else:
        print('NO')
