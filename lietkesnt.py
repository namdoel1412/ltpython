def isPrime(n):
    square = int(n**0.5)+1
    for i in range(2, square):
        if(n%i==0):
            return False
    return True

n = int(input())
lst = [int(x) for x in input().split()]
res = {}
for i in range(n):
    if isPrime(lst[i]) == True:
        if lst[i] in res:
            res[lst[i]]+=1
        else:
            res[lst[i]]=1
for j in range(n):
    if lst[j] in res:
        print(lst[j], end=' ')
        print(res[lst[j]])
        res.pop(lst[j])


