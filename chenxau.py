xau1 = input()
xau2 = input()
k = int(input())-1
length1 = len(xau1)
length2 = len(xau2)
for i in range(0, k):
    print(xau1[i], end='')
print(xau2, end='')
for i in range(k, length1):
    print(xau1[i], end='')
