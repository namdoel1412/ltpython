req = input()
length = len(req)
res = ''
for i in range(length-1, -1, -1):
    # print(req[i], end='')
    res = req[i] + res
    if (length - i)%3 == 0 and i != 0:
        # print(',', end='')
        res = ',' + res
print(res)