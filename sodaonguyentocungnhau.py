def prime_together(num1, num2):
    while(num2 > 0):
        tmp = num2
        num2 = num1%num2
        num1 = tmp
    if num1 == 1:
        return True
    return False



n = int(input())
for i in range(0, n):
    inp = input()
    num1 = int(inp)
    num2 = int(inp[::-1])
    if prime_together(num1, num2):
        print('YES')
    else:
        print('NO')

