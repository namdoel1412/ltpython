def prime_together_N(num1, num2):
    while(num2 > 0):
        tmp = num1%num2
        num1 = num2
        num2 = tmp
    if num1 == 1:
        return True
    return False

lst = [int(i) for i in input().split()]
N = lst[0]
k = lst[1]
count = 0
for i in range(pow(10, k-1), pow(10, k)-1):
    if prime_together_N(i, N):
        count+=1
        if(count == 10):
            print(i)
            count = 0
        else:
            print(i, end=' ')