def isPrime(n):
    if n < 2:
        return False
    tmp = int(n**0.5) + 1
    for i in range(2, tmp):
        if n%i==0:
            return False
    return True

t = int(input())

lst = [int(i) for i in input().split()]
res = []
for item in lst:
    if isPrime(item):
        res.append(item)
res = sorted(res)
k = 0
for item in lst:
    if isPrime(item):
        print(res[k], end=' ')
        k+=1
    else:
        print(item, end=' ')
print()


