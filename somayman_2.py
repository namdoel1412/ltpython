t = int(input())
for i in range(t):
    req = input()
    # length = len(req)
    check = True
    for i in req:
        if i != '4' and i != '7':
            check = False
            break
    if check:
        print('YES')
    else:
        print('NO')