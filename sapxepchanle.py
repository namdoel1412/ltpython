from posixpath import split


t = int(input())
lst = []
while(len(lst) < t):
    for i in input().split():
        lst.append(int(i))

lst1 = []
lst2 = []
for item in lst:
    if item%2==0:
        lst1.append(item)
    else:
        lst2.append(item)

lst1 = sorted(lst1)
lst2 = sorted(lst2, reverse=True)
j = 0
k = 0
for item in lst:
    if item % 2 == 0:
        print(lst1[j], end=' ')
        j+=1
    else:
        print(lst2[k], end=' ')
        k+=1


