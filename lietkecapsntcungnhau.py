t = int(input())

def prime_together(a, b):
    while(b > 0):
        tmp = a%b
        a = b
        b = tmp
    if a == 1:
        return True
    return False


lst = [int(i) for i in input().split()]
res = sorted(lst)
length = len(res)
for j in range(0, length):
    for k in range(j, length):
        if prime_together(res[j], res[k]):
            print(res[j], end=' ')
            print(res[k])