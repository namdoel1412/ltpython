import math
lstP = []
def is_prime(n):
    square = int(n**0.5)+1
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

num = 0
value = 2
while num <= 1000:
    if is_prime(value) == True:
        lstP.append(value)
        num+=1
    value+=1
    
N, X = map(int, input().split())
tmp = X
for i in range(0, N):
    print(tmp, end=' ')
    tmp += lstP[i]
print(tmp)