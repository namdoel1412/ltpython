test = 10
lst = []
while test > 0:
    lstTmp = input().split()
    test -= len(lstTmp)
    for i in lstTmp:
        lst.append(int(i))
dict = {}
for i in lst:
    if i%42 not in dict:
        dict[i%42] = 1
print(len(dict.items()))