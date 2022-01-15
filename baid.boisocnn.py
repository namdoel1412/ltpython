dic = {}
mod = 1000000007
def SangNT(n):
    prime = [True for i in range(n+1)]
    step = 2
    while(step*step < n):
        if(prime[step] == True):
            for j in range(step*2, n+1, step):
                prime[j] = False
        step+=1
    prime[0] = False
    prime[1] = False
    lst = []
    for i in range(n+1):
        if prime[i] == True:
            lst.append(i)
    return lst

primeList = SangNT(100000)

def findUC(a):
    length = len(primeList)
    for i in range(0, length):
        if (a%primeList[i] == 0 and a >= primeList[i]):
            while(a%primeList[i]==0 and a >= primeList[i]):
                a/=primeList[i]
                #print(primeList[i])
                if(primeList[i] not in dic):
                    dic[primeList[i]] = 1
                else:
                    dic[primeList[i]]+=1
        if(a < primeList[i]):
            break


n = int(input())
for i in range(0, n):
    dic = {}
    lst = [int(i) for i in input().split()]
    a = lst[0]
    b = lst[1]
    final = 1
    for j in range(a, b+1):
        final = ((final%mod)*j)%mod
    findUC(final)
    res = 1
    for item in dic.keys():
        if(dic[item] > 0):
            res *= (dic[item]+1)%mod
            res = res%mod
    result = 1
    result = pow(2, res-1, mod)
    # for i in range(0, res-1):
    #     result = ((result%mod)*2)%mod

    print((result+1)%mod)