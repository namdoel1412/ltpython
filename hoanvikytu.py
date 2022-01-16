inp = input()
length = len(inp)
lst = [i for i in range(1, length+1)]

def hienThi():
    for i in range(0, length):
        print(inp[lst[i]-1], end=' ')
    print()

while(True):
    hienThi()
    j = length-2
    while j >= 0 and lst[j] >= lst[j+1]:
        j-=1
    if j < 0:
        break
    for k in range(length-1, j, -1):
        if lst[k] > lst[j]:
            lst[j], lst[k] = lst[k], lst[j]
            break

    l = j+1
    r = length-1
    while l <= r:
        lst[l], lst[r] = lst[r], lst[l]
        l+=1
        r-=1

