def isPrime(n):
    if n < 2:
        return False
    tmp = int(n**0.5)+1
    for i in range(2, tmp):
        if n%i == 0:
            return False
    return True

t = int(input())
lst = [int(i) for i in input().split()]
maxx = 0
for item in lst:
    tmp1 = item
    tmp2 = item
    pre = 0
    nex = 0
    while isPrime(tmp1) == False and tmp1 >= 0:
        tmp1-=1
        pre+=1
    while isPrime(tmp2) == False and tmp2 >= 0:
        tmp2+=1
        nex+=1
    res = pre
    if nex < pre:
        res = nex
    if maxx < res:
        maxx = res

print(maxx)

