lst = [int(i) for i in input().split()]
lst1 = sorted(list(dict.fromkeys([int(i) for i in input().split()])))
lst2 = sorted(list(dict.fromkeys([int(i) for i in input().split()])))
length1 = len(lst1)
length2 = len(lst2)
dic = {}
for item in lst1:
    if item not in dic:
        dic[item] = 1
for item in lst2:
    if item not in dic:
        dic[item] = 3
    else:
        dic[item] = 2

for item in dic.keys():
    if dic[item] == 2:
        print(item, end=' ')
print()

for item in dic.keys():
    if dic[item] == 1:
        print(item, end=' ')
print()

for item in dic.keys():
    if dic[item] == 3:
        print(item, end=' ')
print()