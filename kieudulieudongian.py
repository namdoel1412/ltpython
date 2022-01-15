def extractSNT(a):
    res = 0
    for i in range(2, a+1):
        while a%i==0:
            a/=i
            res+=i
        if a < i:
            break
    return res


t = int(input())
multi = 1
for i in range(0, t):
    n = int(input())
    multi*=extractSNT(n)
print(multi)
