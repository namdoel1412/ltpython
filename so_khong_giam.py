t = int(input())
for i in range(t):
    res = True
    str = input()
    for c in range(0, len(str)-1):
        if str[c] > str[c+1]:
            res = False
            break
    if res == True:
        print('YES')
    else:
        print('NO')
