t = int(input())
dic = {}
for i in range(0, t):
    inp = input()
    if inp.lower() not in dic:
        dic[inp.lower()] = inp.lower()
lst = []
for item in dic.keys():
    lst.append(dic[item])
lst2 = sorted(lst) # can have reverse
for item in lst2:
    print(item)
