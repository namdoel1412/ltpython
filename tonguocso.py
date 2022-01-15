# def sangNTO(n):
#     prime = [True for i in range(0, n+1)]
#     step = 2
#     while(step*step < n):
#         if(prime[step] == True):
#             for i in range(step**2, n, step):
#                 prime[i] = False
#         step+=1
#     prime[0] = False
#     prime[1] = False
#     res = []
#     for i in range(2, n):
#         if prime[i] == True:
#             res.append(i)
#     return res

# lstPrime = sangNTO(1000000)

def extractSNT(a):
    res = 0
    tmp = int((a+1)/2) +1
    for i in range(2, tmp):
        if(a >= i and a%i == 0):
            while(a%i==0):
                a/=i
                res+=i
        if a < i:
            break
    if a > 1:
        res+=a
    return res

t = int(input())
sum = 0
for i in range(0, t):
    n = int(input())
    sum+=extractSNT(n)
print(sum)


