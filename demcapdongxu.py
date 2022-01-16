t = int(input())
lstX = [0 for i in range(0, t)]
lstY = [0 for i in range(0, t)]
for i in range(0, t):
    inp = input()
    count = 0
    for j in range(0, t):
        if inp[j] == 'C':
            count+=1
            lstY[j] += 1
    lstX[i] = count
res = 0
for item in lstX:
    res += int((item-1)*item/2)
for item in lstY:
    res += int((item-1)*item/2)
print(res)


        