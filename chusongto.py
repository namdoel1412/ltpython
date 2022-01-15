t = int(input())

def isPrime(n):
    if n < 2:
        return False
    tmp = int(n**0.5)+1
    for i in range(2, tmp):
        if n%i == 0:
            return False
    return True


for i in range(0, t):
    n = input()
    length = len(n)
    res = True
    count = 0
    if isPrime(length) == False:
        print('NO')
        continue
    else:
        for j in range(0, length):
            if isPrime(int(n[j])) == True:
                count+=1
        if count <= length-count:
            print('NO')
            continue
    print('YES')

    
            