t = int(input())

for i in range(0, t):
    inp = input()
    length = len(inp)
    tong = 0
    res = []
    for j in range(0, length):
        if ord(inp[j]) >= ord('0') and ord(inp[j]) <= ord('9'):
            tong += int(inp[j])
        else:
            res.append(inp[j])
    lst = sorted(res)
    for item in lst:
        print(item, end='')
    print(tong)

