inp = input()
length = len(inp)
if length % 2 != 0:
    inp = inp[:-1]
length-=1
res = []
for i in range(0, length-1, 2):
    res += int(inp[i]+inp[i+1])
res = sorted(list(dict.fromkeys(res)))
for item in res:
    print(item, end=' ')
print()

