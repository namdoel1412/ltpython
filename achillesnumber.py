dic = {}
def extractSNT(n):
    lst = []
    for i in range(2, n+1):
        while(n%i==0):
            n/=i
            lst.append(i)
            if i not in dic:
                dic[i] = 1
        if n < i:
            break
    return lst
    
def check(n):
    for item in dic.keys():
        if n!= item and n%(item**2)!=0:
            return False
    return True

def check2(n):
    res = 0
    for i in range(1, int(n/2)+2):
        if n%i == 0:
            res += i
    if res == n:
        return True
    return False


n = int(input())
extractSNT(n)
# print(check(n))
# print(check2(n))
if check(n) and check2(n) == False:
    print(1)
else:
    print(0)




