inp = input()
length = len(inp)
res = True
lt = 0
for i in range(0, length):
    if inp[i] != '6' and inp[i] != '8':
        res = False
        break
    if inp[i] == '6':
        lt = 0
    if inp[i] == '8':
        lt+=1
    
    if lt == 1 and (i == 0 or inp[i-1] != '6'):
        res = False
        break
    
    if lt == 2 and inp[i-2] != '6':
        res = False
        break

    if lt > 2:
        res = False
        break
if res:
    print('YES')
else:
    print('NO')
