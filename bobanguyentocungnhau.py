def prime_together(num1, num2):
    while(num2 > 0):
        tmp = num1%num2
        num1 = num2
        num2 = tmp
    if(num1 == 1):
        return True
    return False


lst = [int(i) for i in input().split()]
L = lst[0]
R = lst[1]
dic = {}
for i in range(L, R+1):
    for j in range(i+1, R+1):
        if prime_together(i, j):
            if (i, j) not in dic:
                dic[(i, j)] = 5

for i in range(L, R+1):
    for j in range(i+1, R+1):
        if (i, j) in dic:
            for k in range(j+1, R+1):
                if (j, k) in dic and (i, k) in dic:
                    print('(' + str(i) + ', ' + str(j) + ', ' + str(k) + ')')
