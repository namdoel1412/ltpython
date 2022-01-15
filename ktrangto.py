t = int(input())

def isPrime(n):
    if n < 2:
        return False
    tmp = int(n**0.5)+1
    for i in range(2, tmp):
        if n%i==0:
            return False
    return True

for i in range(0, t):
    inp = input()
    length = len(inp)   
    res = ""
    for j in range(length-4, length):
        res += inp[j]
    num = int(res)
    #print(num)
    if isPrime(num):
        print('YES')
    else:
        print('NO')


