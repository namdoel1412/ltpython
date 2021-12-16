t = int(input())
for i in range(t):
    tmp = input()
    length = len(tmp)
    res = False
    if length >= 2 and tmp[length - 2] == '8' and tmp[length - 1] == '6':
        res = True
    if res == True:
        print('YES')
    else:
        print('NO')
            