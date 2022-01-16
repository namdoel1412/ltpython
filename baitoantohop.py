nk = [int(i) for i in input().split()]
lst = sorted(list(dict.fromkeys([int(i) for i in input().split()])))

n = len(lst)
k = nk[1]
res = []
for i in range(1, k+1):
    res.append(i)

def hienThi():
    for i in range(0, k):
        print(lst[res[i]-1], end=' ')
    print()

while(True):
    hienThi()
    j = k-1
    while res[j] == n-k+j+1 and j >= 0:
        j-=1
    if j == -1:
        break
    res[j]+=1
    for l in range(j+1, k):
        res[l] = res[j]+l-j

