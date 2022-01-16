def isPrime(n):
    if n < 2:
        return False
    tmp = int(n**0.5)+1
    for i in range(2, tmp):
        if n%i == 0:
            return False
    return True

t = int(input())
lst = list(dict.fromkeys([int(i) for i in input().split()]))

length = len(lst)
check = True
for i in range(1, length):
    sum1 = 0
    sum2 = 0
    for j in range(0, i):
        sum1+=lst[j]
    for j in range(i, length):
        sum2+=lst[j]
    if isPrime(sum1) and isPrime(sum2):
        print(i-1)
        check = False
        break
if check == True:
    print('NOT FOUND')

    

